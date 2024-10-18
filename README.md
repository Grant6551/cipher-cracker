# 🔐 Cipher Cracker 🔓

Welcome to the **Cipher Decrypting Tool**! This tool allows you to decrypt messages encrypted with a Caesar Cipher by trying every possible key and outputting the results.

---

## 🚀 Features

- 🔍 **Decrypt Caesar Cipher Messages:** The tool will try every possible key to decrypt the message you provide.
- 📝 **Formatted Output:** See the decrypted message for each key to find the correct one.
- 💻 **Interactive CLI:** Enter your message directly into the terminal and view results for every decryption key.
- 🖼️ **Centered Text Design:** Aesthetically pleasing console design with centered text.

---

## 🛠️ Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Grant6551/cipher-cracker.git
   cd caesar-cipher
   ```

2. **Run the program**:

   ```bash
   python caesar-cracker.py
   ```

3. **Input your message**: When prompted, type the message you want to decrypt. The program will display the decrypted message for every possible key.

---

### 📊 Example Output:

```
--------------------- Welcome To Caesar Cipher Decrypting Tool ----------------------

[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|------------|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $S`?a,     |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|       `?a, |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
[ .------ . .---..   ..----  .----:   .-----  .---. .---. .----- |  /  .---- .---. ]
[ |       | |___||__ ||____  | ,,,;   |       | ,,; |___| |      |-@_  |____ | ,,; ]
[ |______ | |    |   ||____  |  \     |_____  |  \  |   | |_____ |   \ |____ |  \  ]
[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|------------|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| _____ _____|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\_____ ____/ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
[---------------------------------------------------------------------- bY z3r0_c001]

--------------------------------------------------------------------------------
                           Enter your Message to Decrypt:
--------------------------------------------------------------------------------
$Decryptor> QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
--------------------------------------------------------------------------------
              Key #0: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
              Key #1: PDA MQEYG XNKSJ BKT FQILO KRAN PDA HWVU ZKC
--------------------------------------------------------------------------------
.
.
.
--------------------------------------------------------------------------------
              Key #23: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
              Key #24: SGD PTHBJ AQNVM ENW ITLOR NUDQ SGD KZYX CNF
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
              Key #25: RFC OSGAI ZPMUL DMV HSKNQ MTCP RFC JYXW BME
--------------------------------------------------------------------------------
...
```

---

## 🎨 Customization

- **Width Adjustment:** The `width` variable is set to 80 by default, which centers the text within a standard console window. Feel free to adjust this according to your preference.
- **Custom Input Prompt:** The program includes a custom prompt that lets users type their message with the style `$Decryptor>`.

---

## 📂 Code Breakdown

### Main Components:

1. **Text Design:** Adds a fun, centered banner for a cool visual.
2. **Decryption Logic:** Loops through each possible key in the Caesar Cipher and prints the decrypted message for every key.
3. **Interactive CLI:** The program interacts with the user, requesting a message and showing results in a clean, centered format.

### 🔧 Decryption Algorithm:

For each possible key, the program shifts the letters of the input message backwards by that key’s value. It handles uppercase letters and symbols like punctuation, leaving non-alphabetical characters unchanged.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request for any improvements or additional features.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🎉 **Enjoy decrypting!** 🔑
