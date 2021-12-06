//-/-/-/-/ Code by: Ricardo Adolfo Gonzalez Teran /-/-/-/-
//ID: A01769410
//Instituto Tecnologico de Estudios Superiores de Monterrey C_Toluca
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <conio.h>
#include <windows.h>
#include <stdlib.h>

using namespace std;


string text_file_1 = "transmission1.txt";
string text_file_2 = "transmission2.txt";
string malicious_text_1 = "mcode1.txt";
string malicious_text_2 = "mcode2.txt";
string malicious_text_3 = "mcode3.txt";

vector<string> t1;
string transmission_1;

vector<string> t2;
string transmission_2;

vector<string> m1;
string mcode1;

vector<string> m2;
string mcode2;

vector<string> m3;
string mcode3;

string mirror_code = "";

vector<int> indexes;

string lcs = "";

void open_transmission1(){

    ifstream file;
    file.open(text_file_1);

    if(file.is_open()){

        while(file.good()){

            file >> text_file_1;
            t1.push_back(text_file_1);

        }

        for(int i = 0; i < t1.size(); i++){

            transmission_1.append(t1[i]);

        }

    }

    else{
        cout << "The file " << text_file_2 << " doesnt exist in the directory..." << endl;
    }

}

void open_transmission2(){

    ifstream file;
    file.open(text_file_2);

    if(file.is_open()){

        while(file.good()){

            file >> text_file_2;
            t2.push_back(text_file_2);

        }

        for(int i = 0; i < t2.size(); i++){

            transmission_2.append(t2[i]);

        }

    }

    else{
        cout << "The file " << text_file_2 << " doesnt exist in the directory..." << endl;
    }

}

void open_malicious_code_1(){

    ifstream file;
    file.open(malicious_text_1);

    if(file.is_open()){

        while(file.good()){

            file >> malicious_text_1;
            m1.push_back(malicious_text_1);

        }

        for(int i = 0; i < m1.size(); i++){

            mcode1.append(m1[i]);

        }

    }

    else{
        cout << "The file " << malicious_text_1 << " doesnt exist in the directory..." << endl;
    }

}

void open_malicious_code_2(){

    ifstream file;
    file.open(malicious_text_2);

    if(file.is_open()){

        while(file.good()){

            file >> malicious_text_2;
            m2.push_back(malicious_text_2);

        }

        for(int i = 0; i < m2.size(); i++){

            mcode2.append(m2[i]);

        }

    }

    else{
        cout << "The file " << malicious_text_2 << " doesnt exist in the directory..." << endl;
    }

}

void open_malicious_code_3(){

    ifstream file;
    file.open(malicious_text_3);

    if(file.is_open()){

        while(file.good()){

            file >> malicious_text_3;
            m3.push_back(malicious_text_3);

        }

        for(int i = 0; i < m3.size(); i++){

            mcode3.append(m3[i]);

        }

    }

    else{
        cout << "The file " << malicious_text_3 << " doesnt exist in the directory..." << endl;
    }

}

void transmission_checker(){

    cout << "----------------------------------------------" << endl;
    cout << "         TRANSMISSION ANALYZER V1.0           " << endl;
    cout << "----------------------------------------------" << endl;
    cout << "----------------------------------------------" << endl;
    
    Sleep(500);
    cout << "             READING FILE 1...               " << endl;
    Sleep(500);
    cout << "Done..." << endl;
    Sleep(200);

    cout << "             READING FILE 2...               " << endl;
    Sleep(500);
    cout << "Done..." << endl;
    Sleep(200);

    cout << "             READING FILE 3...               " << endl;
    Sleep(500);
    cout << "Done..." << endl;
    Sleep(200);

    cout << "             READING FILE 4...               " << endl;
    Sleep(500);
    cout << "Done..." << endl;
    Sleep(200);
    
    cout << "             READING FILE 5...               " << endl;
    Sleep(500);
    cout << "Done..." << endl;
    Sleep(200);

}

//------------------ PART 1 ------------------------------

//--COMPLEGITY OF THE ALGORITHM = O(m+n) or O(m)----------

int pattern_checker(string string_, string pattern){

    //m is the string lenght
    //n is the pattern lenght

    int m = string_.length();
    int n = pattern.length();

    bool success = false;

    // If the pattern is empty returns 0
    if (n == 0) {
        cout << "The pattern is empty" << endl;
        return 0;
    }

    // if the string length is less than pattern lenght returns not found
    if (m < n){
        cout << "Pattern not found";
        return -1;
    }

    // Store the next match
    int next[n + 1];

    for (int i = 0; i < n + 1; i++) {
        next[i] = 0;
    }

    for (int i = 1; i < n; i++){

        int j = next[i + 1];

        while (j > 0 and pattern[j] != pattern[i]){
            j = next[j];
        }

        if (j > 0 or pattern[j] == pattern[i]){
            next[i + 1] = j + 1;
        }

    }

    for (int i = 0, j = 0; i < m; i++){

        if (string_[i] == pattern[j]){

            if (++j == n) {

                indexes.push_back(i - j + 1 + 1);
                success = true;

            }

        }
        else if (j > 0){

            j = next[j];
            i = i-1;

        }
        
    }

    if (success == true){
        return 14;
    }

    else{
        return -1;
    }
    
}

void transmission1_file(){

    cout << "----------------------------------------------" << endl;
    cout << "              TRANSMISSION 1 FILE             " << endl;

//---------------------- Transmission 1 with Malicious Code 1 ------------------

    int tr1_mc1;
    tr1_mc1 = pattern_checker(transmission_1, mcode1);

    if(tr1_mc1 == -1){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 1 CORRUPTION BY MCODE 1 FILE: [FALSE]" << endl;
        cout << "NOTES: The 'mcode1.txt' file is not contained in the 'transmission1.txt' file" << endl << endl;

        indexes.clear();
    }

    if(tr1_mc1 == 14){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 1 CORRUPTION BY MCODE 1 FILE: [TRUE]" << endl;
        cout << "NOTES: The 'mcode1.txt' file is contained in the 'transmission1.txt' file in the position(s): ";

        for(int i = 0; i < indexes.size(); i++){
            cout << indexes[i];
        }

        cout << endl << endl;

        indexes.clear();

    }

//---------------------- Transmission 1 with Malicious Code 1 ------------------

//---------------------- Transmission 1 with Malicious Code 2 ------------------

    int tr1_mc2;
    tr1_mc2 = pattern_checker(transmission_1, mcode2);

    if(tr1_mc2 == -1){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 1 CORRUPTION BY MCODE 2 FILE: [FALSE]" << endl;
        cout << "NOTES: The 'mcode2.txt' file is not contained in the 'transmission1.txt' file" << endl << endl;

        indexes.clear();

    }

    if(tr1_mc2 == 14){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 1 CORRUPTION BY MCODE 2 FILE: [TRUE]" << endl;
        cout << "NOTES: The 'mcode2.txt' file is contained in the 'transmission1.txt' file in the position(s): ";

        for(int i = 0; i < indexes.size(); i++){
            cout << indexes[i];
        }

        cout << endl << endl;

        indexes.clear();


    }

//---------------------- Transmission 1 with Malicious Code 2 ------------------

//---------------------- Transmission 1 with Malicious Code 3 ------------------


    int tr1_mc3;
    tr1_mc3 = pattern_checker(transmission_1, mcode3);

    if(tr1_mc3 == -1){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 1 CORRUPTION BY MCODE 3 FILE: [FALSE]" << endl;
        cout << "NOTES: The 'mcode3.txt' file is not contained in the 'transmission1.txt' file" << endl << endl;

        indexes.clear();

    }

    if(tr1_mc3 == 14){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 1 CORRUPTION BY MCODE 3 FILE: [TRUE]" << endl;
        cout << "NOTES: The 'mcode3.txt' file is contained in the 'transmission1.txt' file in the position(s): ";

        for(int i = 0; i < indexes.size(); i++){
            cout << indexes[i];
        }

        cout << endl << endl;

        indexes.clear();

    }

    cout << "----------------------------------------------" << endl;

//---------------------- Transmission 1 with Malicious Code 3 ------------------




}

void transmission2_file(){

    cout << "----------------------------------------------" << endl;
    cout << "              TRANSMISSION 2 FILE             " << endl;

//---------------------- Transmission 2 with Malicious Code 1 ------------------

    int tr2_mc1;
    tr2_mc1 = pattern_checker(transmission_2, mcode1);

    if(tr2_mc1 == -1){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 2 CORRUPTION BY MCODE 1 FILE: [FALSE]" << endl;
        cout << "NOTES: The 'mcode1.txt' file is not contained in the 'transmission2.txt' file" << endl << endl;

        indexes.clear();
    }

    if(tr2_mc1 == 14){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 2 CORRUPTION BY MCODE 1 FILE: [TRUE]" << endl;
        cout << "NOTES: The 'mcode1.txt' file is contained in the 'transmission2.txt' file in the position(s): ";

        for(int i = 0; i < indexes.size(); i++){
            cout << indexes[i];
        }

        cout << endl << endl;

        indexes.clear();

    }

//---------------------- Transmission 2 with Malicious Code 1 ------------------

//---------------------- Transmission 2 with Malicious Code 2 ------------------

    int tr2_mc2;
    tr2_mc2 = pattern_checker(transmission_2, mcode2);

    if(tr2_mc2 == -1){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 2 CORRUPTION BY MCODE 2 FILE: [FALSE]" << endl;
        cout << "NOTES: The 'mcode2.txt' file is not contained in the 'transmission2.txt' file" << endl << endl;

        indexes.clear();
    }

    if(tr2_mc2 == 14){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 2 CORRUPTION BY MCODE 2 FILE: [TRUE]" << endl;
        cout << "NOTES: The 'mcode2.txt' file is contained in the 'transmission2.txt' file in the position(s): ";

        for(int i = 0; i < indexes.size(); i++){
            cout << indexes[i];
        }

        cout << endl << endl;

        indexes.clear();

    }


//---------------------- Transmission 2 with Malicious Code 2 ------------------

//---------------------- Transmission 2 with Malicious Code 3 ------------------

    int tr2_mc3;
    tr2_mc3 = pattern_checker(transmission_2, mcode3);

    if(tr2_mc3 == -1){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 2 CORRUPTION BY MCODE 3 FILE: [FALSE]" << endl;
        cout << "NOTES: The 'mcode3.txt' file is not contained in the 'transmission2.txt' file" << endl << endl;

        indexes.clear();
    }

    if(tr2_mc3 == 14){

        cout << "----------------------------------------------" << endl;
        cout << "TRANSMISSION 2 CORRUPTION BY MCODE 3 FILE: [TRUE]" << endl;
        cout << "NOTES: The 'mcode3.txt' file is contained in the 'transmission2.txt' file in the position(s): ";

        for(int i = 0; i < indexes.size(); i++){
            cout << indexes[i];
        }

        cout << endl << endl;

        indexes.clear();

    }

    cout << "----------------------------------------------" << endl;

//---------------------- Transmission 2 with Malicious Code 3 ------------------
}


//--COMPLEGITY OF THE ALGORITHM = O(N^3)------------------
int longest_palindrome(string str){

    int len = str.length();
    int max_lenght = 1;
    int start = 0;
    int low; 
    int high;

    for (int i = 1; i < len; ++i) {

        low = i - 1;
        high = i;

        while (low >= 0 and high < len and str[low] == str[high]) {
            
            low = low - 1;
            high = high + 1;

        }

        low = low + 1; 
        high = high - 1;

          if (str[low] == str[high] and high - low + 1 > max_lenght) {

            start = low;

             max_lenght = high - low + 1;

        }

        low = i - 1;
        high = i + 1;

        while (low >= 0 and high < len and str[low] == str[high]) {

            low = low - 1;
            high = high + 1;

        }

        low = low + 1;  
        high = high - 1;

          if (str[low] == str[high] and high - low + 1 > max_lenght) {

            start = low;

             max_lenght = high - low + 1;

        }

    }

    int ans = max_lenght;

    while(ans--)

        mirror_code.push_back(str[start++]);

    return start - max_lenght;
}

//------------------ PART 1 ------------------------------


//------------------ PART 2 ------------------------------

//--COMPLEGITY OF THE ALGORITHM = O(N^2)------------------

int mirrored_code_for(string file_name, string file){

    int mirror_code_start;
    mirror_code_start = longest_palindrome(file);

    int mirror_code_end;
    mirror_code_end = mirror_code_start + mirror_code.size();

    cout << "The start position of the mirrored code in '" << file_name << "' file is: [" << mirror_code_start << "]" << endl;

    cout << "The mirrored code in the '" << file_name << "' file is: [" << mirror_code << "]" << endl;

    cout << "The end position of the mirrored code in '" << file_name << "' file is: [" << mirror_code_end << "]" << endl;

    mirror_code.clear();

}

//------------------ PART 2 ------------------------------


//------------------ PART 3 ------------------------------

//--COMPLEGITY OF THE ALGORITHM = O((m + n) × m^2)--------

int similarity_checker(string file_1, string file_2, int file_1_len, int file_2_len){
    
    // Stores the max length of the lcs
    int max_len = 0;
    // Stores the ending index of LCS in file 1
    int end_index = file_1_len;
 
    //Stores the file 1 and file 2 strings
    int matrix[file_1_len + 1][file_2_len + 1];

    //Init all with zeros to fill later with the characters
    memset(matrix, 0, sizeof(matrix));
    
    //Check the 2 strings with a cicle for
    for(int i = 1; i <= file_1_len; i++){

        for(int j = 1; j <= file_2_len; j++){

            if(file_1[i - 1] == file_2[j - 1]){
             matrix[i][j] = matrix[i - 1][j - 1] + 1;
 
                if(matrix[i][j] > max_len){

                    max_len = matrix[i][j];
                    end_index = i;
                
                }
            }
        }
    }

    lcs = file_1.substr(end_index - max_len, max_len);
 
    return end_index - max_len;
}

//------------------ PART 3 ------------------------------


int main(){

    system("CLS");
    system("Color 03");

    // Intro Operations

    open_transmission1();
    open_transmission2();
    open_malicious_code_1();
    open_malicious_code_2();
    open_malicious_code_3();

    // Part 1

    transmission_checker();
    transmission1_file(); //(3)
    Sleep(2000);
    transmission2_file(); //(3)
    Sleep(2000);
    cout << endl;

    //Part 2
    
    system("Pause");

    cout << endl << endl << endl;
    cout << "----------------------------------------------" << endl;
    cout << "              MIRRORED CODE CHECKER           " << endl;
    cout << "----------------------------------------------" << endl;

    cout << "----------------------------------------------" << endl;
    cout << "              TRANSMISSION 1 FILE             " << endl << endl;
    mirrored_code_for("transmission1.txt", transmission_1);
    cout << "----------------------------------------------" << endl;

    cout << "----------------------------------------------" << endl;
    cout << "              TRANSMISSION 2 FILE             " << endl << endl;
    mirrored_code_for("transmission2.txt", transmission_2);
    cout << "----------------------------------------------" << endl << endl;

    //Part 3

    system("Pause");

    int t1_len = transmission_1.length();
    int t2_len = transmission_2.length();

    
    cout << endl << endl << endl;
    cout << "----------------------------------------------" << endl;
    cout << "              SIMILARITY CODE CHECKER         " << endl;
    cout << "----------------------------------------------" << endl;

    int sc_t1 = similarity_checker(transmission_1, transmission_2, t1_len, t2_len);

    cout << "The start position of the similar code snippet in transmission 1 file is: " << sc_t1 << endl;

    int sc_t2 = similarity_checker(transmission_2, transmission_1, t2_len, t1_len);
    
    cout << "The start position of the similar code snippet in transmission 2 file is: " << sc_t2 << endl;
    
    cout << endl;

    cout << "The transmission files are similarity through the next code snippet: [";

    cout << lcs << "]" << endl << endl;

    cout << "The end position of the similar code snippet in transmission 1 file is: " << sc_t1 + lcs.length() << endl;

    cout << "The end position of the similar code snippet in transmission 2 file is: " << sc_t2 + lcs.length() << endl << endl << endl;

    system("Pause");



    

    






}

