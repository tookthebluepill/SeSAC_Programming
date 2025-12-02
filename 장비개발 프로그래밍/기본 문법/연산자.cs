class 연산자
{
// sizeof 연산자와 char 자료형의 크기
    static void Main12(string[] args)
    {
        Console.WriteLine("int: " + sizeof(int));
        Console.WriteLine("long: " + sizeof(long));
        Console.WriteLine("float: " + sizeof(float));
        Console.WriteLine("double: " + sizeof(double));
        Console.WriteLine("char: " + sizeof(char));
    }
// 증감 연산자
    static void Main13(string[] args)
    {
        int number = 10;
        Console.WriteLine(number);
        Console.WriteLine(number++);
        Console.WriteLine(number--);
        Console.WriteLine(number);
    }
}