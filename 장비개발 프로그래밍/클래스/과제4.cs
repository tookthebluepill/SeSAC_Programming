using System;
using System.Collections.Generic;

namespace FriendManager
{
    class Friend
    {
        public string Name;
        public string Phone;
        public string Memo;

        public Friend(string name, string phone, string memo)
        {
            Name = name;
            Phone = phone;
            Memo = memo;
        }
    }

    class Program
    {
        static List<Friend> friends = new List<Friend>();

        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("\n1. 친구추가 2.친구삭제 3.전체출력 4.종료");
                Console.Write("메뉴>");
                string menu = Console.ReadLine();

                switch (menu)
                {
                    case "1":
                        AddFriend();
                        break;
                    case "2":
                        DeleteFriend();
                        break;
                    case "3":
                        PrintAll();
                        break;
                    case "4":
                        Console.WriteLine("프로그램을 종료합니다.");
                        return;
                    default:
                        Console.WriteLine("1~4번까지 정수만 입력하세요.");
                        break;
                }
            }
        }

        // 메뉴 1. 친구 추가
        static void AddFriend()
        {
            Console.WriteLine("이름, 전화번호, 메모 형식으로 입력>");
            string input = Console.ReadLine();
            string[] parts = input.Split(',');

            if (parts.Length == 3)
            {
                friends.Add(new Friend(parts[0].Trim(), parts[1].Trim(), parts[2].Trim()));
                Console.WriteLine("친구정보 추가 완료!");
            }
            else
            {
                Console.WriteLine("양식이 조금 어려울 수 있습니다.\n맨 처음, 이름을 입력하시고 콤마(,)를 입력하세요. 그 후 다음 정보를 입력하시면 됩니다.\n양식은 이름, 전화번호, 메모로 총 3개가 있습니다.");
            }
        }

        // 메뉴 2. 친구 삭제
        static void DeleteFriend()
        {
            Console.Write("삭제 대상 번호>");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int index))
            {
                if (index >= 0 && index < friends.Count)
                {
                    friends.RemoveAt(index);
                    Console.WriteLine("삭제 완료되었습니다.");
                }
                else
                {
                    Console.WriteLine("존재하지 않는 번호입니다.");
                }
            }
            else
            {
                Console.WriteLine("숫자를 입력해주세요.");
            }
        }

        // 메뉴 3. 전체 출력
        static void PrintAll()
        {
            if (friends.Count == 0)
            {
                Console.WriteLine("등록된 친구가 없습니다.");
                return;
            }

            for (int i = 0; i < friends.Count; i++)
            {
                Console.WriteLine($"{i}, {friends[i].Name}, {friends[i].Phone}, {friends[i].Memo}");
            }
        }
    }
}