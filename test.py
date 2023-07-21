1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
#include <iostream>
using namespace std;
 
struct kaf
{
std::string code; // код кафедры
std::string name; //имя кафедры
int time_plane;  //план. время
int time_fact;   // факт. время
};
 
int main(){
    
    int plan_sum = 0; //общее план по институту
    int fact_sum = 0; //общее факт. по институту
    
    const int kaf_count = 2; // количество кафедр
    kaf *k = new kaf[kaf_count]; //создаем динамически наши 2 кафедры.
    for(int i = 0; i < kaf_count; i++) //заполняем их: шифр, имя, расходы(план и факт)
    {
