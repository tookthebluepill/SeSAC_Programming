class foreach반복문
{
    static void Main(string[] args)
    {
        string[] array = {"사과", "배", "포도", "딸기", "바나나"};
        foreach(string item in array)
        {
            Console.WriteLine(item);
        }
    }
}