function encryptMessage() {
    const message = document.getElementById('message').value;
    const shift = parseInt(document.getElementById('shift').value, 10);
    const encryptedMessage = encrypt(message, shift);
    document.getElementById('output').innerText = encryptedMessage;
}

function decryptMessage() {
    const message = document.getElementById('message').value;
    const shift = parseInt(document.getElementById('shift').value, 10);
    const decryptedMessage = decrypt(message, shift);
    document.getElementById('output').innerText = decryptedMessage;
}

function encrypt(message, shift) {
    let result = '';
    for (let i = 0; i < message.length; i++) {
        let char = message[i];
        if (char.match(/[a-z]/i)) {
            const code = message.charCodeAt(i);
            if ((code >= 65) && (code <= 90)) {
                char = String.fromCharCode(((code - 65 + shift) % 26) + 65);
            } else if ((code >= 97) && (code <= 122)) {
                char = String.fromCharCode(((code - 97 + shift) % 26) + 97);
            }
        }
        result += char;
    }
    return result;
}

function decrypt(message, shift) {
    return encrypt(message, -shift);
}
