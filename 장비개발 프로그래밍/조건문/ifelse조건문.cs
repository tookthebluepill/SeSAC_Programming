class ifelse조건문
{
        static void Main0(string[] args)
        {
            Console.WriteLine("과목을 선택하세요\n(1.C# 2.C 3.C++ 4.Python)");
            Console.Write("과목번호:");
            string? input = Console.ReadLine();
            int code = int.Parse(input);
            if (code == 1)
            {
                Console.WriteLine("R101호 입니다.");
            }
            else if (code == 2)
            {
                Console.WriteLine("R202호 입니다.");
            }
            else if (code == 3)
            {
                Console.WriteLine("R303호 입니다.");
            }
            else if (code == 4)
            {
                Console.WriteLine("R404호 입니다.");
            }
            else
            {
                Console.WriteLine("상담원에게 문의하세요");
            }
        }
}

// ifelse문연습
// 과목번호를 입력받아 강의실 번호를 출력하는 프로그램 작성
// 과목 code값이 1이면 "R101호 입니다."
// 과목 code값이 2이면 "R202호 입니다."
// 과목 code값이 3이면 "R303호 입니다."
// 과목 code값이 4이면 "R404호 입니다."
// 나머지는 "상담원에게 문의하세요"
// 출력

// ex
// 과목을 선택하세요
// (1.Java 2.C 3.C++ 4.Python)
// 과목번호:2
// R202호 입니다!

