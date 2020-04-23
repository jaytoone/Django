
(function() {
  var Needle, arc, arcEndRad, arcStartRad, barWidth, chart, chartInset, degToRad, el, endPadRad, height, i, margin, needle, numSections, padRad, percToDeg, percToRad, percent, radius, ref, sectionIndx, sectionPerc, startPadRad, svg, totalPercent, width, line;
  percent = 0.34; //퍼센트 조정 가능
  barWidth = 110;
  numSections = 0;
  sectionPerc = 1 / numSections / 2;
  padRad = 0;
  chartInset = 0;
  totalPercent = 1;
  el = d3.select('.chart-gauge');
  margin = {
    top: 20,
    right: 20,
    bottom: 30,
    left: 20
  };
  width = el[0][0].offsetWidth - margin.left - margin.right;
  height = width;
  radius = Math.min(width, height) / 2;
  percToDeg = function(perc) {
    return perc * 360;
  };
  percToRad = function(perc) {
    return degToRad(percToDeg(perc));
  };
  degToRad = function(deg) {
    return deg * Math.PI / 180;
  };
  svg = el.append('svg').attr('width', width + margin.left + margin.right).attr('height', height + margin.top + margin.bottom);
  chart = svg.append('g').attr('transform', 'translate(' + (width + margin.left) / 2 + ', ' + (height + margin.top) / 2 + ')');

  arcStartRad = percToRad(totalPercent);
  arcEndRad = arcStartRad + percToRad(sectionPerc);
  totalPercent += 100;

  segment1 = d3.svg.arc().outerRadius(radius - chartInset).innerRadius(radius - chartInset - barWidth).startAngle(-1.58).endAngle(-0.43);
  segment2 = d3.svg.arc().outerRadius(radius - chartInset).innerRadius(radius - chartInset - barWidth).startAngle(-0.43).endAngle(0.00);
  segment3 = d3.svg.arc().outerRadius(radius - chartInset).innerRadius(radius - chartInset - barWidth).startAngle(0.00).endAngle(1.58);
  chart.append('path').attr('class', 'arc chart-color1').attr('d', segment1);
  chart.append('path').attr('class', 'arc chart-color2').attr('d', segment2);
  chart.append('path').attr('class', 'arc chart-color3').attr('d', segment3);

  Needle = function() {
    function Needle(len, radius1) {
      this.len = len;
      this.radius = radius1;
    }
    Needle.prototype.drawOn = function(el, perc) {
      el.append('circle').attr('class', 'needle-center').attr('cx', 0).attr('cy', 0).attr('r', this.radius);
      return el.append('path').attr('class', 'needle').attr('d', this.mkCmd(perc));
    };
    Needle.prototype.animateOn = function(el, perc) {
      var self;
      self = this;
      return el.transition().delay(500).ease('elastic').duration(3000).selectAll('.needle').tween('progress', function() {
        return function(percentOfPercent) {
          var progress;
          progress = percentOfPercent * perc;
          return d3.select(this).attr('d', self.mkCmd(progress));
        };
      });
    };
    Needle.prototype.mkCmd = function(perc) {
      var centerX, centerY, leftX, leftY, rightX, rightY, thetaRad, topX, topY;
      thetaRad = percToRad(perc / 2);
      centerX = 0;
      centerY = 0;
      topX = centerX - this.len * Math.cos(thetaRad);
      topY = centerY - this.len * Math.sin(thetaRad);
      leftX = centerX - this.radius * Math.cos(thetaRad - Math.PI / 2);
      leftY = centerY - this.radius * Math.sin(thetaRad - Math.PI / 2);
      rightX = centerX - this.radius * Math.cos(thetaRad + Math.PI / 2);
      rightY = centerY - this.radius * Math.sin(thetaRad + Math.PI / 2);
      return 'M ' + leftX + ' ' + leftY + ' L ' + topX + ' ' + topY + ' L ' + rightX + ' ' + rightY;
    };
    return Needle;
  }();

  LineDiv = function() {
    function LineDiv(len, radius1) {
      this.len = len;
      this.radius = radius1;
    }
    LineDiv.prototype.drawOn = function(el, perc, strokeWidth, strokeColor) {
      var centerX, centerY, corner1X, corner1Y, corner2X, corner2Y;
      thetaRad = percToRad(perc / 2);
      centerX = 0;
      centerY = 0;
      corner1X = centerX - this.len * Math.cos(thetaRad);
      corner1Y = centerY - this.len * Math.sin(thetaRad);
      corner2X = centerX - this.radius * Math.cos(thetaRad - Math.PI / 2);
      corner2Y = centerY - this.radius * Math.sin(thetaRad - Math.PI / 2);

      el.append('circle').attr('class', 'needle-center').attr('cx', 0).attr('cy', 0).attr('r', this.radius);
      return el.append('line')
        .attr('class', 'line-div')
        .attr('x1', corner1X)
        .attr('y1', corner1Y)
        .attr('stroke', strokeColor)
        .attr('stroke-width', strokeWidth);
    };

    LineDiv.prototype.mkCmd = function(perc) {

    };
    return LineDiv;
  }();

  needle = new Needle(211, 15);

  lineDiv = new LineDiv(230); // param 'lenth'
  lineDiv2 = new LineDiv(230); // param 'lenth'
  lineDiv2.drawOn(chart, 0.50, 5, '#ffffff'); // params; element, radius(%), stroke, color
  lineDiv.drawOn(chart, 0.36, 5, '#ffffff'); // params; element, radius(%), stroke, color
  needle.drawOn(chart, 0);
  needle.animateOn(chart, percent);

}.call(this));
