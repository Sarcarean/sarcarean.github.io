//Uses the p5.js example code for the particle effect
//Modified and additional code by rharris7@cocc.edu for CS-161

var systems;
var pail_img;

function setup() {
  createCanvas(600, 400);   //Create frame
  systems = [];
  pail_img = loadImage("./images/pail.png");  // Load the image
}
	
function draw() {
	//background(255);
	background('lightblue');
	noStroke();
	for (i = 0; i < systems.length; i++) {
		systems[i].run();
		systems[i].addParticle();
	}
    fill(0,0,128);
    textAlign(CENTER);
	if (systems.length==0) {   //Nothing to show
		textSize(32); 
		text("Click Mouse to begin the app!", width/2, height/2);
	} else {
		image(pail_img, systems[0].origin.x-90, systems[0].origin.y-60);
		textSize(16);
		text("Use the arrow keys to move the pail", width/2, 20);
	}
}

function mousePressed() {
  if (systems.length==0) {   //Start the show
	this.p = new ParticleSystem(createVector(width/2, height/2)); //Place effect in middle of screen
	systems.push(p);
  }
}

function keyPressed() {
	if (systems.length>0) {
		if (keyCode === LEFT_ARROW) {
			systems[0].origin.x -= 12;
		} else if (keyCode === RIGHT_ARROW) {
			systems[0].origin.x += 12;
		} else if (keyCode === UP_ARROW) {
			systems[0].origin.y -= 12;
		} else if (keyCode === DOWN_ARROW) {
			systems[0].origin.y += 12;
		}
	}
}

var Particle = function(position) {
  this.acceleration = createVector(0, 0.05);
  this.velocity = createVector(random(-1, 1), random(-1, 0));
  this.position = position.copy();
  this.lifespan = 255.0;
};

Particle.prototype.run = function() {
  this.update();
  this.display();
};

Particle.prototype.update = function(){
  this.velocity.add(this.acceleration);
  this.position.add(this.velocity);
  this.lifespan -= 2;
};

Particle.prototype.display = function () {
  stroke(200, this.lifespan);
  strokeWeight(2);
  fill(127, this.lifespan);
  ellipse(this.position.x, this.position.y, 12, 12);
};

Particle.prototype.isDead = function () {
  if (this.lifespan < 0) {
    return true;
  } else {
    return false;
  }
};

var ParticleSystem = function (position) {
  this.origin = position.copy();
  this.particles = [];
};

ParticleSystem.prototype.addParticle = function () {
  if (int(random(0, 2)) == 0) {
    p = new Particle(this.origin);
  }
  else {
    p = new CrazyParticle(this.origin);
  }
  this.particles.push(p);
};

ParticleSystem.prototype.run = function () {
  for (var i = this.particles.length - 1; i >= 0; i--) {
    var p = this.particles[i];
    p.run();
    if (p.isDead()) {
      this.particles.splice(i, 1);
    }
  }
};

function CrazyParticle(origin) {
  Particle.call(this, origin);
  this.theta = 0.0;
};

CrazyParticle.prototype = Object.create(Particle.prototype); // See note below

CrazyParticle.prototype.constructor = CrazyParticle;

CrazyParticle.prototype.update=function() {
  Particle.prototype.update.call(this);
  this.theta += (this.velocity.x * this.velocity.mag()) / 10.0;
}

CrazyParticle.prototype.display=function() {
  Particle.prototype.display.call(this);
  push();
  translate(this.position.x, this.position.y);
  rotate(this.theta);
  stroke(255,this.lifespan);
  pop();
}
