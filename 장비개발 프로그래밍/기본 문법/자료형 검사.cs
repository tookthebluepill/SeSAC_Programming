class 자료형검사
{
        static void Main0(string[] args)
    {
        int number=10;
        Console.WriteLine(number);
    }
// GetType() 메서드를 활용해 자료형을 출력
        static void Main(string[] args)
    {
        int _int = 273;
        long _long = 522731033265;
        float _float = 52.273F;
        double _double = 52.273;

        char _char = '글';
        string _string = "문자열";

        Console.WriteLine(_int.GetType());
        Console.WriteLine(_long.GetType());
        Console.WriteLine(_float.GetType());
        Console.WriteLine(_double.GetType());
        Console.WriteLine(_char.GetType());
        Console.WriteLine(_string.GetType());
    }    
// 직접적인 GetType() 메서드 활용
        static void Main2(string[] args)
    {   
        Console.WriteLine((273).GetType());
        Console.WriteLine((522731033265L).GetType());
        Console.WriteLine((52.273F).GetType());
        Console.WriteLine((52.273).GetType());
        Console.WriteLine(('자').GetType());
        Console.WriteLine(("문자열").GetType());
    }
}