// class Lunchmate
// {
//   static void Main(string[] args)
//   {
//     string[] mate = new string[]{"강동호", "김재현", "성찬", 
//                                   "김지니수", "서재윤", "임현택", 
//                                   "한민수", "안가빈", "임수인",
//                                   "박하연", "김동수", "이성진",
//                                   "이승연", "김민지", "김민찬",
//                                   "이형주", "최재빈","김용찬" };
    
//     for(int i = 0; i < mate.Length; i++)
//     {
//       if(i % 3 == 0)
//       {
//         Console.Write("\n " + mate[i]);
//       }
//       else
//       {
//         Console.Write(", " + mate[i]);
//       }
      
//     }
//   }
// }


// class Lunchmate2
// {
//   static void Main(string[] args)
//   {
//     string[] mate = new string[]{"강동호", "김재현", "성찬", 
//                                   "김지니수", "서재윤", "임현택", 
//                                   "한민수", "안가빈", "임수인",
//                                   "박하연", "김동수", "이성진",
//                                   "이승연", "김민지", "김민찬",
//                                   "이형주", "최재빈","김용찬" };
    
//     // 점심파트너 결정( 0 ~ 17 )
//     int[] mateNumber = new int[18];

//     Random rand = new Random();
//     for (int i = 0; i < 18; i++)
//     {
//       // 최초 i==0 일때는 그냥 넣기
//       if(i == 0)
//       {
//         mateNumber[i] = rand.Next(1, 19);
//       } else { // i==1 부터 이전값 비교 ( j 부터 i 까지 )
//         mateNumber[i] = rand.Next(1, 19);
//         for (int j = 0; j < i; j++)
//         {
//           // 이전값과 비교해서 같은것 발견시 i=1 j=0
//           if (mateNumber[i] == mateNumber[j])
//           {
//             i--;
//             break;
//           }
//         }
//       }
//     }

//     // for (int i = 0; i < 18; i++)
//     // {
//     //   Console.WriteLine(mateNumber[i]);
//     // }

//     // 점심 파트너 출력
//     for(int i = 0; i < mate.Length; i++)
//     {
//       if(i % 3 == 0)
//       {
//         Console.Write("\n " + mate[i]);
//       }
//       else
//       {
//         Console.Write(", " + mate[i]);
//       }
//     }
    
//     // 중복 검증
//     for (int i = 0; i < 18; i++)
//     {
//       for (int j = i + 1; j < 18; j++)
//       {
//         if (mateNumber[i] == mateNumber[j])
//         {
//           Console.WriteLine("중복!");
//           return;
//         }
//       }
//     } 
//   }
// }