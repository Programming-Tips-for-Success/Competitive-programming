
function solution(A, B, P) {
    var contacts = [];
    for (i = 0; i < B.length; i++) {

        if (B[i].includes(P)) {
            contacts.push(A[i]);
        }

    }

    sortedContacts.sort()
    let finalContact = !sortedContacts.length ? "NO CONTACT" :
        sortedContacts[0];
    return finalContact;
}
