class 응용예제
{

    // 대문자화와 소문자화
    static void Main0(string[] args)
    {
        string input = "Potato Tomato";
        Console.WriteLine(input.ToUpper());
        Console.WriteLine(input.ToLower());
    }
    // 문자열 자르기
    static void Main1(string[] args)
    {
        string input = "감자 고구마 토마토";
        string[] inputs = input.Split(new char[] { ' ' });

        foreach (var item in inputs)
        {
            Console.WriteLine(item);
        }
    }

    // 문자열 양옆의 공백 제거
    // Trim(): 문자열 양옆의 공백을 제거
    // TrimStart(): 문자열 앞의 공백을 제거
    // TrimEnd(): 문자열 뒤의 공백을 제거
    static void Main2(string[] args)
    {
        string input = "test    \n";
        Console.WriteLine("::" + input.Trim() + "::");
    }

    // 배열을 문자열로 변환
    static void Main3(string[] args)
    {
        string[] array = { "감자", "고구마", "토마토", "가지" };
        Console.WriteLine(string.Join(",", array));
    }

    // Console.SetCursorPosition() 메서드
    // 자신이 원하는 위치에 글자를 출력할 수 있음
    static void Main4(string[] args)
    {
        Console.Write("메서드 호출 전");
        Console.SetCursorPosition(5, 5);
        Console.Write("메서드 호출 후");
    }
}