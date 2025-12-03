// 출력 방법
// 방법1: Console 클래스의 WriteLine() 메서드 사용
// Console.Write(출력하고_싶은_대상);
// static void Main(string[] arg)
// {
//     Console.WriteLine("Hello C# Programming!");
// }

public class 출력
{
    static void Main0(string[] args)
    {
        Console.WriteLine("Hello C# Programming ..!");
    }
// 정수
    static void Main1(string[] args)
    {
        Console.WriteLine(52);
    }
// 연산자
    static void Main2(string[] args)
    {
        Console.WriteLine(52+273);
    }
// 문자열
// \t:수평 탭, \\:역슬래시, \n:행 바꿈, \":큰 따옴표
    static void Main3(string[] args)
    {
        Console.WriteLine("다키스트\t던전");
        Console.WriteLine("다키스트\n던전");
        Console.WriteLine("\"\"\"");
    }

// 문자 선택(인덱싱)
    static void Main31(string[] args)
    {
        Console.WriteLine("제육덮밥"[0]);
        Console.WriteLine("제육덮밥"[1]);
        Console.WriteLine("제육덮밥"[3]);
        Console.WriteLine("제육덮밥"[^1]); //^:끝에서부터 인덱싱
        Console.WriteLine("제육덮밥"[100]); //예외 발생
    }

// 슬라이싱
// 범위로 ..을 사용하여 표현한다
    static void Main32(string[] args)
    {
        string s = "Hello World";
        string slice = s[^8..^5];
        Console.WriteLine(slice);
    }


    static void Main44(string[] args)
    {
        Console.WriteLine('ナ');
        Console.WriteLine('リ');
        Console.WriteLine('タ');
        Console.WriteLine('A');
        Console.WriteLine('ㅗ');
    }

// 문자 덧셈 연산
// 문자는 + 연산자를 사용해도 연결되지 않음
    static void Main5(string[] args)
    {
        Console.WriteLine('가' + '나');
    }
// 오버플로
// 2,147,483,647에 1을 더하면 int 자료형의 범위를 넘어버리면서 -2,147,483,648이 됨
    static void Main6(string[] args)
    {
        int a = 2147483640;
        int b = 52273;
        Console.WriteLine(a+b);
    }

    static void Main7(string[] args)
    {
        int a = 2147483640;
        int b = 52273;
        Console.WriteLine(a+b);
    }
    static void Main8(string[] args)
    {
        uint unsignedA = 200000000;
        uint unsignedB = 100000000;
        Console.WriteLine(unsignedA+unsignedB);
    }
// unsigned 자료형
// int 자료형은 -2147483648부터2147483647까지 나타낼 수 있음
// 음수를 사용하지 않는다면 -2147483648부터 -1까지의 숫자가 낭비됨
// 이런 낭비를 막고자 C#은 unsigned 자료형(부호가 없는 자료형)을 제공
// int와 long 키워드 대신 uint와 ulong 키워드를 사용    
    static void Main9(string[] args)
    {
        uint unsignedInt = 4147483647;
        ulong unsignedLong = 11223372036854775808;
        
        Console.WriteLine(unsignedInt);
        Console.WriteLine(unsignedLong);
    }
// 최댓값과 최솟값
    static void Main10(string[] args)
    {
        Console.WriteLine(int.MaxValue);
        Console.WriteLine(int.MinValue);
    }

    static void Main11(string[] args)
    {
        Console.WriteLine(long.MaxValue);
        Console.WriteLine(long.MinValue);
    }

    static void Main12(string[] args)
    {
        Console.WriteLine(1.0 + 2.0);
        Console.WriteLine(1.0 - 2.0);
        Console.WriteLine(1.0 * 2.0);
        Console.WriteLine(1.0 / 2.0);
        Console.WriteLine(7.0/3.0);
        Console.WriteLine(7.0/3);
        Console.WriteLine(7/3.0);
        Console.WriteLine(5.0%2.2);
    }

}