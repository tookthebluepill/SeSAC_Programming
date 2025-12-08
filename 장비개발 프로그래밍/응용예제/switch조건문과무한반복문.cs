class SwitchWithWhile
{
    static void Main0(string[] args)
    {
        while (true)
        {
            ConsoleKeyInfo info = Console.ReadKey();
            switch (info.Key)
            {
                case ConsoleKey.UpArrow:
                    Console.WriteLine("위로 이동");
                    break;
                case ConsoleKey.RightArrow:
                    Console.WriteLine("오른쪽으로 이동");
                    break;
                case ConsoleKey.DownArrow:
                    Console.WriteLine("아래로 이동");
                    break;
                case ConsoleKey.LeftArrow:
                    Console.WriteLine("왼쪽으로 이동");
                    break;
                case ConsoleKey.X:
                    break;
            }
        }
    }

    // switch 조건문 내부의 break 키워드는 switch 조건문만 벗어남
    // goto 대신 조건을 추가하면 while 반복문까지 벗어남
    static void Main(string[] args)
    {
        bool state = true;
        while (state)
        {
            ConsoleKeyInfo info = Console.ReadKey();
            switch (info.Key)
            {
                case ConsoleKey.UpArrow:
                    Console.WriteLine("위로 이동");
                    break;
                case ConsoleKey.RightArrow:
                    Console.WriteLine("오른쪽으로 이동");
                    break;
                case ConsoleKey.DownArrow:
                    Console.WriteLine("아래로 이동");
                    break;
                case ConsoleKey.LeftArrow:
                    Console.WriteLine("왼쪽으로 이동");
                    break;
                case ConsoleKey.X:
                    state = false;
                    break;
            }
        }
    }

}

// 코드 포맷팅
// shift + alt + F를 누르면 자동 줄 맞춤을 해준다