interface Point {

    x: number;

    y: number;

    distance(other: Point): number;

}


// Classes are the implementations:

class PointImplementation implements Point {

    public x: number;

    public y: number;


    constructor(x: number, y: number) {

        this.x = x;

        this.y = y;

    }


    public distance(other: Point): number {

        return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));

    }

}

