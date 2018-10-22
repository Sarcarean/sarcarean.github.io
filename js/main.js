var x = 100;
var y = 100;
var xspeed = 5;
var yspeed = 2;

var r = 25;

function setup() {
  createCanvas(620, 200);
}

function draw() {
  background('blue');
  ellipse(x, y, r*2, r*2);
  x += xspeed;
  y += yspeed;
  if (x > width - r || x < r) {
    xspeed = -xspeed;
  }
  if (y > height - r || y < r) {
    yspeed = -yspeed;
  }

}