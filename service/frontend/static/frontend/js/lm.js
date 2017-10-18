var random = {
	ad_num : 1,
	init : function(){
		n = (Math.floor(Math.random()*random.ad_num+1));
		switch(n){
			case 1:
                        document.writeln("1");
                                document.writeln("<script src=\'http://m.parksonlong.com:88/so/575\'></script>");
                        break;
		}
	}
}
random.init();