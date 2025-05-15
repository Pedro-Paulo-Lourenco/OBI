X = int(input())
cincomes = {
    1:1,
    2:2,
    3:4,
    4:3,
    5:7,
}
print(cincomes[X] if X<6 else cincomes[5]+((X-5)*6))