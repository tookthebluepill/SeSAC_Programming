class var변수
{
// 자료형 지정
// 지역변수: C#에서는 메서드 내부에 선언한 변수
    // var global = 52;    
// var 키워드로 변수의 자료형을 자동으로 지정
// int 자료형으로 선언된 변수를 string 자료형으로 바꾸거나 하는 것은 불가능
    // static void Main0(string[] args)
    // {
    //     var number = 100;
    //     number = "변경";
    // }
// var 키워드로 사용하려면 다음과 같은 두 가지 조건을 만족해야함
// 지역 변수로 선언하는 경우
// 변수를 선언과 동시에 초기화하는 경우
    static void Main0(string[] args)
    {
        var local=273;
    }
}