function matchTable(word) {
  let arr = Array.from({ length: word.length }).fill(0);
  let suffixEnd = 1;
  let prefixEnd = 0;
  while (suffixEnd < word.length) {
    if (word[suffixEnd] === word[prefixEnd]) {
      // we can build a longer prefix based on this suffix
      // store the length of this longest prefix
      // move prefixEnd and suffixEnd
      prefixEnd += 1;
      arr[suffixEnd] = prefixEnd;
      suffixEnd += 1;
    } else if (word[suffixEnd] !== word[prefixEnd] && prefixEnd !== 0) {
      // there's a mismatch, so we can't build a larger prefix
      // move the prefixEnd to the position of the next largest prefix
      prefixEnd = arr[prefixEnd - 1];
    } else {
      // we can't build a proper prefix with any of the proper suffixes
      // let's move on
      arr[suffixEnd] = 0;
      suffixEnd += 1;
    }
  }
  return arr;
}

function kmpSearch(long, short) {
  let table = matchTable(short);
  let shortIdx = 0;
  let longIdx = 0;
  let count = 0;
  while (longIdx < long.length - short.length + shortIdx + 1) {
    if (short[shortIdx] !== long[longIdx]) {
      // we found a mismatch :(
      // if we just started searching the short, move the long pointer
      // otherwise, move the short pointer to the end of the next potential prefix
      // that will lead to a match
      if (shortIdx === 0) longIdx += 1;
      else shortIdx = table[shortIdx - 1];
    } else {
      // we found a match! shift both pointers
      shortIdx += 1;
      longIdx += 1;
      // then check to see if we've found the substring in the large string
      if (shortIdx === short.length) {
        // we found a substring! increment the count
        // then move the short pointer to the end of the next potential prefix
        count++;
        shortIdx = table[shortIdx - 1];
      }
    }
  }
  return count;
}

// KMP - O(n + m) time, O(m) space

function print(x){
console.log(x);

}

//  node basic-dsa/kmp-search.js
