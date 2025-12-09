// // 1~45까지의 숫자 중 임의의 6개의 숫자를 출력하시오 (중복체크는 하지 말 것)
// // Random rand = new Random();
// // for (int i =0; i<6; i++)
// // {
// //     int num = rand.Next(1,46);
// //     Console.WriteLine(num);
// // }


// // 1~45까지의 숫자 중 임의의 6개의 숫자를 출력하시오 (중복체크하고 배열에 담기)
// int[] lotto = new int[6];
// Random rand = new Random();
// for (int i = 0; i <6; i++)
// {
//     if(i==0)
//     {
//         lotto[i] = rand.Next(1,46);
//     } else
//     {
//         for(int j=0; j<i; j++)
//         {
            
//         }
//     }
// }

// for (int i=0; i<6; i++)
// {
//     Console.WriteLine(lotto[i]);
// }

// // 1~45 까지의 숫자중 임의의 6개의 숫자를 출력하세요(중복체크)
// int[] lotto = new int[6];

// Random rand = new Random();
// for (int i = 0; i < 6; i++)
// {
//   // 최초 i==0 일때는 그냥 넣기
//   if(i == 0)
//   {
//     lotto[i] = rand.Next(1, 46);
//   } else { // i==1 부터 이전값 비교 ( j 부터 i 까지 )
//     lotto[i] = rand.Next(1, 46);
//     for (int j = 0; j < i; j++)
//     {
//       // 이전값과 비교해서 같은것 발견시 i=1 j=0
//       if (lotto[i] == lotto[j])
//       {
//         i--;
//         break;
//       }
//     }
//   }
// }

// for (int i = 0; i < 6; i++)
// {
//   Console.WriteLine(lotto[i]);
// }