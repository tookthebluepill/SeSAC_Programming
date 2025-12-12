interface IShape
{
  public double compute();
}

class Ractangle : IShape
{
  public double width;
  public double height;
  public Ractangle(double width, double height)
  {
    this.width = width;
    this.height = height;
  }

  public double compute()
  {
    return width * height;
  }
}

class Triangle : IShape
{
  public double width;
  public double height;
  public Triangle(double width, double height)
  {
    this.width = width;
    this.height = height;
  }

  public double compute()
  {
    return width * height / 2;
  }
}

class Circle : IShape
{
  public double radius;
  public Circle(double radius)
  {
    this.radius = radius;
  }

  public double compute(){
    return Math.PI * radius * radius;
  }
}

class Program
{
  static void Main(string[] args)
  {
    IShape r = new Ractangle(3,3);
    IShape t = new Triangle(3,3);
    IShape c = new Circle(2);

    Console.WriteLine($"사각형({((Ractangle)r).width}, {((Ractangle)r).height})의 면적은 : " + r.compute());
    Console.WriteLine($"삼각형({((Triangle)t).width}, {((Triangle)t).height})의 면적은 : " + t.compute());
    Console.WriteLine($"원({((Circle)c).radius})의 면적은 : " + c.compute());
  }
}