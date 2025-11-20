def cook_ramen(water, ramen, soup):
    print(f"{water}ml 물에 {ramen}과 {soup}을 넣습니다.")

#위치 매개변수
cook_ramen(500, "신라면", "매운맛 스프")

#키워드 매개변수
cook_ramen(ramen = "신라면", soup="매운맛 스프", water=500)
cook_ramen(soup="순한맛 스프", ramen="너구리", water=600)