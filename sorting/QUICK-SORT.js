// function quickSort(data) {
//     if (Array.Length <= 1)
//       return;
//     middle = Array[Array.Length / 2];
//     let left = new Array();
//     let right = new Array();
//     for (let i = 0; i < Array.length; i++)
//       if (i != Array.Length / 2) {
//         if (Array[i] <= middle)
//           left.Add(Array[i]);
//         else
//           right.Add(Array[i]);
//       }
//     return concatenate(quickSort(left), middle, quickSort(right));
//     }