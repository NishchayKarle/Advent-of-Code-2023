#define CS 13
#define SK 12
#define DI 11
#define DO 10
#define ORGGRND 9

#define SBAUD 115200
#define CMDMSK8 0b1000000000 // 0x200
#define CMDMSK16 0b100000000 // 0x100

bool bitmode8;

void setup()
{
    bitmode8 = true;

    pinMode(CS, OUTPUT);
    pinMode(SK, OUTPUT);
    pinMode(DI, OUTPUT);
    pinMode(ORGGRND, OUTPUT);

    Serial.begin(SBAUD);
    Serial.print("SBAUD: ");
    Serial.println(SBAUD);
    Serial.println("COLD BOOT");

    Serial.println("8 BIT MODE");

    digitalWrite(CS, LOW);
    digitalWrite(SK, LOW);
    digitalWrite(DI, LOW);
    digitalWrite(ORGGRND, LOW);
}

void loop()
{
    Serial.println("93C46 TEST MENU");
    Serial.println("1 - Read All");
    Serial.println("2 - EWEN Write Enable");
    Serial.println("3 - EWDS Write DISable");
    Serial.println("4 - WRAL 0xA5");
    Serial.println("5 - ERAL Erase ALL");
    Serial.println("6 - Write  0:12,34,56,78,9A,BC,DE,FA");
    Serial.println("7 - Write  0:22,44,66,88,AA,BB,CC,DD");
    Serial.println("8 - Erase  0, 3,4, 7");
    Serial.println("9 - Write Ascii String at LOC 0");
    Serial.println("s - Switch to other module");
    Serial.println("w - Write ASCII string at input LOC");
    Serial.println("CDM: ");
    while (!Serial.available())
    {
    };

    int val;

    char ch = Serial.read();
    Serial.print("INPUT CMD: ");
    Serial.println(ch);

    switch (ch)
    {

    case '1':
    {
        Serial.println("Read All");
        int len = 128;
        if (!bitmode8)
            len = 64;

        for (int i = 0; i < len; i++)
        {
            if (i % 16 == 0)
                Serial.println();

            val = NVRead(i);
            if (32 <= val and val <= 126)
                Serial.print((char)val);
            else
                Serial.print(val, HEX);
            Serial.print(" ");
        }
        Serial.println();
    }

    break;

    case '2':
        Serial.println("EWEN Write Enable");
        NVEwen();
        break;

    case '3':
        Serial.println("EWDS Write Disable");
        NVEwds();
        break;

    case '4':
        Serial.println("WRAL Write ALL = 0xA5");
        NVWral(0xA5);
        break;

    case '5':
        Serial.println("ERAL Erase ALL");
        NVEral();
        break;

    case '6':
        Serial.println("Write  0:12,34,56,78,9A,BC,DE,FA");
        NVWrite(0, 0x12);
        NVWrite(1, 0x34);
        NVWrite(2, 0x56);
        NVWrite(3, 0x78);
        NVWrite(4, 0x9A);
        NVWrite(5, 0xBC);
        NVWrite(6, 0xDE);
        NVWrite(7, 0xFA);
        break;

    case '7':
        Serial.println("Write  0:22,44,66,88,AA,BB,CC,DD");
        NVWrite(0, 0x22);
        NVWrite(1, 0x44);
        NVWrite(2, 0x66);
        NVWrite(3, 0x88);
        NVWrite(4, 0xAA);
        NVWrite(5, 0xBB);
        NVWrite(6, 0xCC);
        NVWrite(7, 0xDD);
        break;

    case '8':
        Serial.println("Erase  0, 3,4, 7");
        NVErase(0);
        NVErase(3);
        NVErase(4);
        NVErase(7);
        break;

    case '9':
    {
        Serial.print("Input ASCII String: ");
        while (!Serial.available())
        {
        };
        String inputStr = Serial.readString();
        Serial.println(inputStr);

        int maxloc = 128;
        if (!bitmode8)
            maxloc = 64;

        for (int i = 0; i < min(inputStr.length(), maxloc); i++)
            NVWrite(i, inputStr[i]);

        break;
    }

    case 's':
        switchModes();

        Serial.print("SWITCHED MODE TO: ");
        if (bitmode8)
            Serial.println("8 bit");
        else
            Serial.println("16 bit");

        break;
    
    case 'w':
    {
        int maxloc = 128;
        if (!bitmode8)
            maxloc = 64;

        Serial.print("Input Write Location: ");
        while (!Serial.available()) {};
        int loc = Serial.parseInt();
        Serial.println(loc);

        if (loc >= maxloc or loc < 0)
        {
            Serial.println("Invalid Location");
            break;
        }

        Serial.print("Input ASCII String: ");
        while (!Serial.available())
        {
        };
        String inputStr = Serial.readString();
        Serial.println(inputStr);

        for (int i = 0; i < min(inputStr.length(), maxloc); i++)
            NVWrite(i + loc, inputStr[i]);
        
        break;
    }

    default:
        Serial.print("INVALID COMMAND: ");
        Serial.println(ch);
        break;
    }
}

void switchModes()
{
    bitmode8 ^= true;
    digitalWrite(ORGGRND, (int)!bitmode8);
}

void cmdout(int oprnd, int msk)
{
    int len = 10;
    if (!bitmode8)
        len = 9;

    for (byte j = 0; j < len; j++)
    {
        if (oprnd & msk)
            digitalWrite(DI, HIGH);

        else
            digitalWrite(DI, LOW);

        digitalWrite(SK, HIGH);

        oprnd <<= 1;

        digitalWrite(SK, LOW);
    }
}

int datain(byte c)
{
    int v = 0;
    for (byte j = 0; j < c; j++)
    {
        v <<= 1;

        digitalWrite(SK, HIGH);
        v |= digitalRead(DO);
        digitalWrite(SK, LOW);
    }

    return v;
}

void dataout(int val, byte c)
{
    int msk;

    if (c == 8)
        msk = 0b10000000;
    else
        msk = 0b1000000000000000;

    for (byte j = 0; j < c; j++)
    {
        if (val & msk)
            digitalWrite(DI, HIGH);
        else
            digitalWrite(DI, LOW);

        digitalWrite(SK, HIGH);
        val <<= 1;
        digitalWrite(SK, LOW);
    }
}

int NVRead(byte addrs)
{
    int oprnd = 0b1100000000 + addrs,
        bits = 8,
        msk = CMDMSK8;

    if (!bitmode8)
    {
        bits = 16;
        oprnd = 0b110000000 + addrs;
        msk = CMDMSK16;
    }

    // Serial.print("READ Operand: ");
    // Serial.println(oprnd);

    digitalWrite(CS, HIGH);

    cmdout(oprnd, msk);
    int v = datain(bits);

    digitalWrite(CS, LOW);

    return v;
}

void NVEwen()
{
    int oprnd = 0b1001100000,
        msk = CMDMSK8;

    if (!bitmode8)
    {
        oprnd = 0b100110000;
        msk = CMDMSK16;
    }

    Serial.print("Write Enable Operand: ");
    Serial.println(oprnd);

    digitalWrite(CS, HIGH);
    cmdout(oprnd, msk);
    digitalWrite(CS, LOW);
}

void NVErase(byte addrs)
{
    int oprnd = 0b1110000000 + addrs,
        msk = CMDMSK8;

    if (!bitmode8)
    {
        oprnd = 0b111000000 + addrs;
        msk = CMDMSK16;
    }

    Serial.print("Erase Operand: ");
    Serial.println(oprnd);

    digitalWrite(CS, HIGH);
    cmdout(oprnd, msk);
    digitalWrite(CS, LOW);

    digitalWrite(CS, HIGH);
    while (!digitalRead(DO))
    {
    };
    digitalWrite(CS, LOW);
}

void NVWrite(byte addrs, int val)
{
    int oprnd = 0b1010000000 + addrs,
        msk = CMDMSK8,
        bits = 8;

    if (!bitmode8)
    {
        oprnd = 0b101000000 + addrs;
        msk = CMDMSK16;
        bits = 16;
    }
    Serial.print("Write Operand: ");
    Serial.println(oprnd);

    digitalWrite(CS, HIGH);

    cmdout(oprnd, msk);
    dataout(val, bits);

    digitalWrite(CS, LOW);

    digitalWrite(CS, HIGH);
    while (!digitalRead(DO))
    {
    };
    digitalWrite(CS, LOW);
}

void NVEral()
{
    int oprnd = 0b1001000000,
        msk = CMDMSK8;

    if (!bitmode8)
    {
        oprnd = 0b100100000;
        msk = CMDMSK16;
    }

    Serial.print("Erase All Operand: ");
    Serial.println(oprnd);

    digitalWrite(CS, HIGH);
    cmdout(oprnd, msk);
    digitalWrite(CS, LOW);

    digitalWrite(CS, HIGH);
    while (!digitalRead(DO))
    {
    };
    digitalWrite(CS, LOW);
}

void NVWral(int val)
{
    int oprnd = 0b1000100000,
        msk = CMDMSK8,
        bits = 8;

    if (!bitmode8)
    {
        oprnd = 0b100010000;
        msk = CMDMSK16;
        bits = 16;
    }

    Serial.print("Write All Operand: ");
    Serial.println(oprnd);

    digitalWrite(CS, HIGH);

    cmdout(oprnd, msk);
    dataout(val, bits);

    digitalWrite(CS, LOW);

    digitalWrite(CS, HIGH);
    while (!digitalRead(DO))
    {
    };
    digitalWrite(CS, LOW);
}

void NVEwds()
{
    int oprnd = 0b1000000000,
        msk = CMDMSK8;

    if (!bitmode8)
    {
        oprnd = 0b100000000;
        msk = CMDMSK16;
    }

    Serial.print("Write Disable Operand: ");
    Serial.println(oprnd);

    digitalWrite(CS, HIGH);
    cmdout(oprnd, msk);
    digitalWrite(CS, LOW);
}
