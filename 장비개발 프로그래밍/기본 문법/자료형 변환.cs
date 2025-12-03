class 자료형변환
{
// 강제 자료형 변환
    static void Main0(string[] args)
    {
        long longNumber = 2147483647L + 2147483647L;
        int intNumber = (int)longNumber;
        Console.WriteLine(intNumber);
    }
// 큰 자료형에서 작은 자료형으로 변환할 때 숫자가 넘쳐 없어질 수 있다.

// 다른 자료형을 숫자로 숫자로 변환할 사용하는 메서드
// int.Parse(): 다른 자료형을 int 자료형으로 변경
// long.Parse(): 다른 자료형을 long 자료형으로 변경
// float.Parse(): 다른 자료형을 float 자료형으로 변경
// double.Parse(): 다른 자료형을 double 자료형으로 변경
// bool.Parse(): 문자열을 bool 자료형으로 변환

// 다른 자료형을 문자열로 변환할 때는 ToString() 메서드를 사용
    static void Main1(string[] args)
    {
        Console.WriteLine((52.273).ToString());
    }
// 숫자와 문자열 덧셈
    static void Main2(string[] args)
    {
        Console.WriteLine(52+273);
        Console.WriteLine("52"+273);
        Console.WriteLine(52+"273");
        Console.WriteLine("52"+"273");
    }
}