
/* -------------  makes drug_abuse tilt on mouseover  ---------------------- */

$(document).ready(function(){
  $("#drug_abuse").mouseover(function(){
      $("#drug_abuse").addClass("left_angled");
  });
});

$(document).ready(function(){
  $("#drug_abuse").mouseleave(function(){
      $("#drug_abuse").removeClass("left_angled");
  });
});

/* -------------  makes depression tilt on mouseover  ---------------------- */

$(document).ready(function(){
  $("#depression").mouseover(function(){
      $("#depression").addClass("right_angled");
  });
});

$(document).ready(function(){
  $("#depression").mouseleave(function(){
      $("#depression").removeClass("right_angled");
  });
});


/* -------------  makes stress tilt on mouseover  ---------------------- */
$(document).ready(function(){
  $("#stress").mouseover(function(){
      $("#stress").addClass("left_angled");
  });
});

$(document).ready(function(){
  $("#stress").mouseleave(function(){
      $("#stress").removeClass("left_angled");
  });
});

/* -------------  makes eating_disorder tilt on mouseover  ---------------------- */
$(document).ready(function(){
  $("#eating_disorder").mouseover(function(){
      $("#eating_disorder").addClass("right_angled");
  });
});

$(document).ready(function(){
  $("#eating_disorder").mouseleave(function(){
      $("#eating_disorder").removeClass("right_angled");
  });
});
