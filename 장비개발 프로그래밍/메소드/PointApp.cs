// Point 클래스
// x, y 좌표를 나나낼 수 있는 필드 작성 int형
// x, y 좌표에 접근할 수 있는 메소드 작성 public int getX()
// 다음 실행 결과를 참조하여 draw() 메소드 작성

// 점[x=5, y=5]을 그렸습니다.
// 점[x=10, y=23]을 그렸습니다.

// Point 클래스 draw(bool delete)를 오버로딩 하세요
// 기존에 만들어진 draw()를 오버로딩 하여 draw(bool delete) 만들고
// 지웠습니다 메시지를 출력하도록 구현

// 점[x=5, y=5]를 지웠습니다.

// class Point
// {
//     public int x, y;
//     public void draw()
//     {
//         Console.WriteLine($"점 [x={x}, y={y}]을 그렸습니다.");
//     }
//     public void draw(bool delete)
//     {
//         if (delete)
//         {
//             Console.WriteLine($"점 [x={x}, y={y}]을 지웠습니다.");
//         }
//         else
//         {
//             draw();
//         }
//     }
//     static void Main(string[] args)
//     {
//         Point p1 = new Point();
//         Point p2 = new Point();
//         p1.x = 5;
//         p1.y = 5;
//         p2.x = 10;
//         p2.y = 23;

//         p1.draw();
//         p2.draw();

//         p1.draw(true);
//         p2.draw(true);
//     }
// }

class Program
{
    class Point
    {
        private int x, y;
        public static int count = 0;
        public Point(int x, int y)
        {
            Point.count++;
            this.x = x;
            this.y = y;
        }
        public Point()
        {
            Point.count++;
        }

        public int getX() { return x; }
        public int getY() { return y; }

        public void setX(int x)
        {
            this.x = x;
        }
        public void setY(int y)
        {
            this.y = y;
        }

        public void draw()
        {
            Console.WriteLine("점 [x = " + this.getX() + ", y = " + this.getY() + "]을 그렸습니다.");
        }
        public void draw(bool delete)
        {
            if (delete)
            {
                Console.WriteLine("점 [x = " + this.getX() + ", y = " + this.getY() + "]을 지웠습니다.");
            }

        }
    }
    static void Main(string[] args)
    {
        Point p1 = new Point();
        Point p2 = new Point();

        //p1.x = 5;
        p1.setX(5);
        //p1.y = 5;
        p1.setY(5);

        p2.setX(10);
        p2.setY(23);

        p1.draw();
        p2.draw();

        p1.draw(true);
        p2.draw(true);

        p1.draw(false);
        Console.WriteLine("점의 개수는 " + Point.count + "개입니다.");
    }
}