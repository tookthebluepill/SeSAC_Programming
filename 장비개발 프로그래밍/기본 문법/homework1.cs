class homework1
{
    static void Main0(string[] args)
    {
        string? input = Console.ReadLine();
        if (string.IsNullOrEmpty(input))
        {
            return;
        }
        int sup = int.Parse(input);
        double hwa = (sup * 9.0 / 5) + 32;
        Console.WriteLine($"섭씨 {sup} 는 화씨 {hwa} 입니다.");
    }
}

