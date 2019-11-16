
module.exports = {
  isAlive: (alive, num) => {
    if ( num == 3 ) return true;
    if ( alive && num == 2 ) return true;
    return false;
  },
  Grid: function(w) {
    this.x = 1;
    this.width =w;
  },
};
