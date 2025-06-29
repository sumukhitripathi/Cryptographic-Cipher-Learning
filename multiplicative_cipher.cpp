/*
multiplicative cipher is a sort of monoalphabetic cipher in which a character in the plaintext 
is multiplied by the key, followed by the modulus function.
Eg: n=4, h->x
*/

#include<iostream>
#include<string>
#include<cctype>
using namespace std;

// Keys valid for multiplicative cipher (must be coprime with 26)
const int keys[] = {1,3,5,7,9,11,13,15,17,19,21,23,25};
const int key_inv[] = {1,9,21,15,3,19,25,7,23,11,5,17,13}; // multiplicative inverses

string encrypt(const string& message, int key){
    string translated = "";
    for (char c : message){
        if (isupper(c)){
            translated += char(((c - 'A') * key) % 26 + 'A');
        }
        else if (islower(c)){
            translated += char(((c - 'a') * key) % 26 + 'a');
        }
        else {
            translated += c;
        }
    }
    return translated;
}

string decrypt(const string& translated, int key){
    string message = "";
    int inv = -1;
    for (int i = 0; i < 13; i++){
        if (keys[i] == key){
            inv = key_inv[i];
            break;
        }
    }
    if (inv == -1) return "Invalid key!";
    
    for (char c : translated){
        if (isupper(c)){
            message += char(((c - 'A') * inv) % 26 + 'A');
        }
        else if (islower(c)){
            message += char(((c - 'a') * inv) % 26 + 'a');
        }
        else {
            message += c;
        }
    }
    return message;
}

int main(){
    string message = "This is a message";
    int key = 7;
    cout << "Original message: " << message << endl;
    string encrypted = encrypt(message, key);
    cout << "Encrypted message: " << encrypted << endl;
    cout << "Decrypted message: " << decrypt(encrypted, key) << endl;
    return 0;
}
