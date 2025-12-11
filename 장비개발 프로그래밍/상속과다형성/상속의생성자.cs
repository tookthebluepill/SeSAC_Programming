// class Program
// {
//     class Parent
//     {
//         public Parent() { Console.WriteLine("Parent()"); }
//         public Parent(int param) { Console.WriteLine("Parent(int Param)"); }
//         public Parent(string param) { Console.WriteLine("Parent(string Param)"); }
//     }

//     class Child : Parent
//     {
//         public Child() : base(10)
//         {
//             Console.WriteLine("Child() : base(10)");
//         }

//         public Child(string input) : base(input)
//         {
//             Console.WriteLine("Child(string input) : base(input)");
//         }
//     }
    
//     static void Main(string[] args)
//     {
//         Child childA = new Child();
//         Child childB = new Child("string");
//     }
// }