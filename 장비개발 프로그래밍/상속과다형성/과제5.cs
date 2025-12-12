// Base App 콘솔 앱
// Base 클래스를 상속하여 MyBase 클래스 작성
// Main()과 Base 클래스는 수정하지 않는다
using System.Security.Cryptography.X509Certificates;

public class Base
{
    public void service(string state)
    {
        if (state == "낮")
        {
            day();
        }
        else
        {
            night();
        }
    }
    public virtual void day()
    {
        Console.WriteLine("낮");
    }
    public virtual void night()
    {
        Console.WriteLine("night");
    }
}
public class MyBase : Base
{

    public override void day()
    {
        Console.WriteLine("낮에는 열심히 일하자");
    }

    public override void night()
    {
        Console.WriteLine("오후도 낮과 마찬가지로 일해야 합니다");
    }
}
public class Program
{
    static void Main(string[] args)
    {
        Base base1 = new Base();
        base1.service("낮");
        base1.service("밤");
        base1.service("오후");

        Base myBase1 = new MyBase();
        myBase1.service("낮");
        base1.service("밤");
        myBase1.service("오후");
    }
}

// class MyBase : Base
// {
//   public void service(string state)
//   {
//     if(state == "낮")
//     {
//       day();
//     }
//     else if(state == "밤")
//     {
//       night();
//     }else if(state == "오후")
//     {
//       afternoon();
//     }
//   }

//   public void afternoon()
//   {
//     Console.WriteLine("오후도 마찬가지로 일해야 합니다");
//   }

//   public void day()
//   {
//     Console.WriteLine("낮에는 열심히 일하자");
//   }
// }