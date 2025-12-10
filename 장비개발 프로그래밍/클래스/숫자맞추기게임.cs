// class NumberGame
// {
//   static void Main(string[] args)
//   {
//     bool isContinue = true;
//     Console.WriteLine("=============================");
//     Console.WriteLine("     [숫자 맟추기 게임]      ");
//     Console.WriteLine("=============================");
//     while (isContinue)
//     {
//       // 숫자 맟추기 게임(1~100)
//       // 게임 종료 여부 묻고 종료 시키기
//       Random random = new Random();
//       int answer = random.Next(1, 101);

//       int input = 0;
//       int count = 0;
      
//       do
//       {
        
//         Console.Write($"{answer} >>");
//         input = int.Parse(Console.ReadLine());
//         count++;

//         if (answer > input)
//         {
//           Console.WriteLine("더 높게");
//         }
//         else if (answer < input)
//         {
//           Console.WriteLine("더 낮게");
//         }
//       } while (answer != input);

//       Console.WriteLine($"맞았습니다( {count}회 )");
//       Console.Write("게임을 종료 하겠습니까?(y/n)");
//       string yn = Console.ReadLine();
//       if (yn == "y")
//       {
//         isContinue = false;
//       }
//     }
      
//     Console.WriteLine("=============================");
//     Console.WriteLine("   [숫자 맟추기 게임종료]    ");
//     Console.WriteLine("=============================");
//   } 
// }