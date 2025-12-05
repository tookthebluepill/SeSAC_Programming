class switch조건문
{
// 월을 입력받아 해당 월이 몇일까지인지 출력
// 1을 입력하면
// 1월을 31일까지 입니다를 출력
// switch 문을 사용할것
    static void Main0(String[] args)
    {
        Console.Write("월을 입력하세요: \n1 ~ 12(숫자로만 입력하세요)");
        string? input = Console.ReadLine();
        int month = int.Parse(input);
        int days = 0;
        {
            switch (month)  
            {
                case 1:
                case 3:
                case 5:
                case 7:
                case 8:
                case 10:
                case 12:
                    days = 31;
                    break;
                
                case 4:
                case 6:
                case 9:
                case 11:
                    days = 30;
                    break;
                
                case 2:
                    days = 28;
                    break;
                
                default:
                    Console.WriteLine("잘못된 월을 입력했습니다. (1~12 사이만 입력)");
                    return;
            }
            Console.WriteLine($"{month}월은 {days}일까지 입니다.");
        }
    }
// 키보드 키 입력 구분
static void Main1(string[] args)
    {
        ConsoleKeyInfo info = Console.ReadKey();
        switch (info.Key)
        {
            case ConsoleKey.UpArrow:
                Console.WriteLine("위쪽으로 이동");
                break;
            case ConsoleKey.RightArrow:
                Console.WriteLine("오른쪽으로 이동");
                break;
            case ConsoleKey.DownArrow:
                Console.WriteLine("아래쪽으로 이동");
                break;
            case ConsoleKey.LeftArrow:
                Console.WriteLine("왼쪽으로 이동");
                break;
            default:
                Console.WriteLine("다른 키를 눌렀습니다");
                break;
        }
    }
}