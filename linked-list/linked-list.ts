class AppComponent {

  head;
  len = 0;


  listprint() {
    let printval = this.head;

    while (printval != null) {
      printval = printval.next;
      this.dataPrint(printval);
    }
  }

  append(elem) {
    let node = new dataNode(elem);
    let current;

    if (!this.head) {
      this.head = node;
    } else {
      current = this.head;
      while (current.next) {
        current = current.next;
      }
      current.next = node;
    }
    this.len++;
  }

  removeNode(Removekey) {
    let HeadVal = this.head;

    if (HeadVal != null) {
      if (HeadVal.dataval == Removekey) {
        this.head = HeadVal.next;

        HeadVal = null;

        return;
      }
      while (HeadVal != null) {
        if (HeadVal.data == Removekey) {
          break;
        }

        let prev = HeadVal;

        HeadVal = HeadVal.next;

        if (HeadVal == null) {
          return;
        }
        prev.next = HeadVal.next;

        HeadVal = null;
      }
    }
  }

  search(x) {
    let current = this.head;

    if (current.elem == x) {
      return true;
    }

    current = current.next;

    return false;
  }

  dataPrint(val){
    console.log(val)
  }
}

class dataNode {
  elem;
  next;

  constructor(elem) {
    this.elem = elem;
    this.next = null;
  }
}

let obj = new AppComponent();
// obj.append(2);
obj.append(4);
obj.append(6);
// obj.removeNode(4);

// let findElement = obj.search(2);
// console.log(findElement);

obj.listprint();

// node linked-list/linked-list.ts
