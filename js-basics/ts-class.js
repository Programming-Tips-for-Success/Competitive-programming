var QuoteModel = /** @class */ (function () {
    function QuoteModel(text, timeCreated) {
        this.text = text;
        this.timeCreated = timeCreated;
    }
    return QuoteModel;
}());
var AppComponent = /** @class */ (function () {
    function AppComponent() {
        this.quoteList = [];
        this.daysOfTheWeeks = ["Sun", "Mon", "Tue", "Wed", "Thurs", "Fri", "Sat"];
        console.log(this.addNewQuote('Motivational')); // {text: "Motivational", timeCreated: "Sat 4, 2020" }
    }
    AppComponent.prototype.addNewQuote = function (quote) {
        var date = new Date();
        var dayOfTheWeek = this.daysOfTheWeeks[date.getDate()];
        var day = date.getDay();
        var year = date.getFullYear();
        this.quoteList.push(new QuoteModel(quote, dayOfTheWeek + " " + day + ", " + year)); // to create objects we can use QuoteModel class
        console.log(this.quoteList);
    };
    return AppComponent;
}());
var User = /** @class */ (function () {
    /**
    * @param {string} username
    @param {Array.<string>} tags
    ***/
    function User(username, tags) {
        this.username = '';
        this.tags = [];
        this.followers = [];
        this.username = username;
        this.tags = tags;
        this.followers = [];
    }
    /**
    * @param {User} user
    @returns void
    ***/
    User.prototype.addFollower = function (user) {
        this.followers.push(user);
    };
    /**
    * Get the followers who are tagged with tag
    @param {string} tag
    * @returns {Array.<User>}
    */
    User.prototype.getFollowers = function (tag) {
        // Fill in this line
        // return this.followers.filter(
        // (follower) => follower.tags.includes (tag));
        // return this. followers.includes (
        //     (follower) => follower.tags.filter(tag)
        //     );
        //     return this.followers.filter(
        // (follower) =>
        // follower.tags.filter((followerTag) => tag ===
        // followerTag
        // ).length > 0
        // );
        // return this.followers.map(
        // (follower) => follower.tags.includes(tag)
        // );
    };
    return User;
}());
var userObj = new User('a', ['1', '2', '3', '4', '5']);
userObj.addFollower('b');
console.log(userObj.getFollowers('2'));
// tsc js-basics/ts-class.ts  
// node js-basics/ts-class.js 
