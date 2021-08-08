"use strict";
exports.__esModule = true;
exports.Node = void 0;
var AppComponent = /** @class */ (function () {
    function AppComponent() {
        this.head = null;
        this.len = 0;
    }
    AppComponent.prototype.listprint = function () {
        var printval = this.head;
        while (printval != null) {
            console.log(printval.elem);
            printval = printval.next;
        }
    };
    AppComponent.prototype.append = function (elem) {
        var node = new Node(elem);
        var current;
        if (this.head === null) {
            this.head = node;
        }
        else {
            current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = node;
        }
        this.len++;
    };
    AppComponent.prototype.removeNode = function (Removekey) {
        var HeadVal = this.head;
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
                var prev = HeadVal;
                HeadVal = HeadVal.next;
                if (HeadVal == null) {
                    return;
                }
                prev.next = HeadVal.next;
                HeadVal = null;
            }
        }
    };
    AppComponent.prototype.search = function (x) {
        var current = this.head;
        if (current.elem == x) {
            return true;
        }
        current = current.next;
        return false;
    };
    return AppComponent;
}());
var Node = /** @class */ (function () {
    function Node(elem) {
        this.elem = elem;
        this.next = null;
    }
    return Node;
}());
exports.Node = Node;
var obj = new AppComponent();
obj.append(2);
obj.append(4);
obj.append(6);
obj.removeNode(4);
var findElement = obj.search(2);
console.log(findElement);
obj.listprint();
