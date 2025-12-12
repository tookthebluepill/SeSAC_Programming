// using System.Data.Common;
// class Animal
// {
//     public int Age { get; set; }
//     // public Animal() { this.Age = 0; }
//     public virtual void Eat() { Console.WriteLine("냠냠 먹습니다."); }
//     // public void Sleep() { Console.WriteLine("쿨쿨 잡니다."); }
// }
// class Dog : Animal
// {
//     public string Color { get; set; }
    
//     public override void Eat()
//     {
//         Console.WriteLine("강아지 사료를 먹습니다.");
//     }
//     // public void Bark() { Console.WriteLine("왈왈 짖습니다."); }
// }
// class Cat : Animal
// {
//     public override void Eat()
//     {
//         Console.WriteLine("고양이 사료를 먹습니다.");
//     }
//     // public void Meow() { Console.WriteLine("냥냥 웁니다."); }
// }

// class Program
// {
//     static void Main(string[] args)
//     {
//         List<Animal> Animals = new List<Animal>()
//     {
//         new Dog(), new Dog(), new Cat(), new Cat()
//     };
//         foreach (var item in Animals)
//         {
//             item.Eat();
//             // item.Sleep();

//             // if (item is Dog dog)
//             // {
//             //     dog.Bark();
//             // }
//             // else if (item is Cat cat)
//             // {
//             //     cat.Meow();
//             // }
//         }
//     }
// }