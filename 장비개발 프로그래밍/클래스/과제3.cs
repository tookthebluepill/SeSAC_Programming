using 과제3;

FishBread fs = new FishBread();
fs.Name = "슈크림붕어빵";
fs.Price = 2000;

FishBread fp = new FishBread();
fp.Name = "팥붕어빵";
fp.Price = 1000;

Console.WriteLine("붕어빵 수량을 입력하세요");

int fpCount;
int fsCount;

Console.Write($"{fp.Name} 개수: ");
fpCount = int.Parse(Console.ReadLine());
Console.Write($"{fs.Name} 개수: ");
fsCount = int.Parse(Console.ReadLine());

long fpTotal = (long)fp.Price * fpCount;
long fsTotal = (long)fs.Price * fsCount;
long totalprice = fpTotal + fsTotal;
Console.WriteLine($"전체 금액은 {totalprice}원입니다");