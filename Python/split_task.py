<!DOCTYPE html>
<html lang="en" >

<head>

	
	<script>
window.ts_endpoint_url = "https:\/\/slack.com\/beacon\/timing";

(function(e) {
	var n=Date.now?Date.now():+new Date,r=e.performance||{},t=[],a={},i=function(e,n){for(var r=0,a=t.length,i=[];a>r;r++)t[r][e]==n&&i.push(t[r]);return i},o=function(e,n){for(var r,a=t.length;a--;)r=t[a],r.entryType!=e||void 0!==n&&r.name!=n||t.splice(a,1)};r.now||(r.now=r.webkitNow||r.mozNow||r.msNow||function(){return(Date.now?Date.now():+new Date)-n}),r.mark||(r.mark=r.webkitMark||function(e){var n={name:e,entryType:"mark",startTime:r.now(),duration:0};t.push(n),a[e]=n}),r.measure||(r.measure=r.webkitMeasure||function(e,n,r){n=a[n].startTime,r=a[r].startTime,t.push({name:e,entryType:"measure",startTime:n,duration:r-n})}),r.getEntriesByType||(r.getEntriesByType=r.webkitGetEntriesByType||function(e){return i("entryType",e)}),r.getEntriesByName||(r.getEntriesByName=r.webkitGetEntriesByName||function(e){return i("name",e)}),r.clearMarks||(r.clearMarks=r.webkitClearMarks||function(e){o("mark",e)}),r.clearMeasures||(r.clearMeasures=r.webkitClearMeasures||function(e){o("measure",e)}),e.performance=r,"function"==typeof define&&(define.amd||define.ajs)&&define("performance",[],function(){return r}) // eslint-disable-line
})(window);

</script>
<script>;(function() {

'use strict';


window.TSMark = function(mark_label) {
	if (!window.performance || !window.performance.mark) return;
	performance.mark(mark_label);
};
window.TSMark('start_load');


window.TSMeasureAndBeacon = function(measure_label, start_mark_label) {
	if (start_mark_label === 'start_nav' && window.performance && window.performance.timing) {
		window.TSBeacon(measure_label, (new Date()).getTime() - performance.timing.navigationStart);
		return;
	}
	if (!window.performance || !window.performance.mark || !window.performance.measure) return;
	performance.mark(start_mark_label + '_end');
	try {
		performance.measure(measure_label, start_mark_label, start_mark_label + '_end');
		window.TSBeacon(measure_label, performance.getEntriesByName(measure_label)[0].duration);
	} catch(e) { return; }
};


window.TSBeacon = function(label, value) {
	var endpoint_url = window.ts_endpoint_url || 'https://slack.com/beacon/timing';
	(new Image()).src = endpoint_url + '?data=' + encodeURIComponent(label + ':' + value);
};

})();
</script>
 

<script>
window.TSMark('step_load');
</script>	<noscript><meta http-equiv="refresh" content="0; URL=/files/varun03/F2JBMRH0R/split_task.py?nojsmode=1" /></noscript>
<script>(function() {
        'use strict';

	var start_time = Date.now();
	var logs = [];
	var connecting = true;
	var ever_connected = false;
	var log_namespace;

	var logWorker = function(ob) {
		var log_str = ob.secs+' start_label:'+ob.start_label+' measure_label:'+ob.measure_label+' description:'+ob.description;

		if (TS.metrics.getLatestMark(ob.start_label)) {
			TS.metrics.measure(ob.measure_label, ob.start_label);
			TS.log(88, log_str);

			if (ob.do_reset) {
				window.TSMark(ob.start_label);
			}
		} else {
			TS.maybeWarn(88, 'not timing: '+log_str);
		}
	}

	var log = function(k, description) {
		var secs = (Date.now()-start_time)/1000;

		logs.push({
			k: k,
			d: description,
			t: secs,
			c: !!connecting
		})

		if (!window.boot_data) return;
		if (!window.TS) return;
		if (!TS.metrics) return;
		if (!connecting) return;

		
		log_namespace = log_namespace || (function() {
			if (boot_data.app == 'client') return 'client';
			if (boot_data.app == 'space') return 'post';
			if (boot_data.app == 'api') return 'apisite';
			if (boot_data.app == 'mobile') return 'mobileweb';
			if (boot_data.app == 'web' || boot_data.app == 'oauth') return 'web';
			return 'unknown';
		})();

		var modifier = (TS.boot_data.feature_no_rollups) ? '_no_rollups' : '';

		logWorker({
			k: k,
			secs: secs,
			description: description,
			start_label: ever_connected ? 'start_reconnect' : 'start_load',
			measure_label: 'v2_'+log_namespace+modifier+(ever_connected ? '_reconnect__' : '_load__')+k,
			do_reset: false,
		});
	}

	var setConnecting = function(val) {
		val = !!val;
		if (val == connecting) return;

		if (val) {
			log('start');
			if (ever_connected) {
				
				window.TSMark('start_reconnect');
				window.TSMark('step_reconnect');
				window.TSMark('step_load');
			}

			connecting = val;
			log('start');
		} else {
			log('over');
			ever_connected = true;
			connecting = val;
		}
	}

	window.TSConnLogger = {
		log: log,
		logs: logs,
		start_time: start_time,
		setConnecting: setConnecting
	}
})();</script>

<script type="text/javascript">
if(self!==top)window.document.write("\u003Cstyle>body * {display:none !important;}\u003C\/style>\u003Ca href=\"#\" onclick="+
"\"top.location.href=window.location.href\" style=\"display:block !important;padding:10px\">Go to Slack.com\u003C\/a>");

(function() {
	var timer;
	if (self !== top) {
		timer = window.setInterval(function() {
			if (window.$) {
				try {
					$('#page').remove();
					$('#client-ui').remove();
					window.TS = null;
					window.clearInterval(timer);
				} catch(e) {}
			}
		}, 200);
	}
}());

</script>

<script>(function() {
        'use strict';

        window.callSlackAPIUnauthed = function(method, args, callback) {
                var timestamp = Date.now() / 1000;  
                var version = (window.TS && TS.boot_data) ? TS.boot_data.version_uid.substring(0, 8) : 'noversion';
                var url = '/api/' + method + '?_x_id=' + version + '-' + timestamp;
                var req = new XMLHttpRequest();

                req.onreadystatechange = function() {
                        if (req.readyState == 4) {
                                req.onreadystatechange = null;
                                var obj;

                                if (req.status == 200 || req.status == 429) {
                                        try {
                                                obj = JSON.parse(req.responseText);
                                        } catch (err) {
                                                console.warn('unable to do anything with api rsp');
                                        }
                                }

                                obj = obj || {
                                        ok: false
                                }

                                callback(obj.ok, obj, args);
                        }
                }

                var async = true;
                req.open('POST', url, async);

                var form_data = new FormData();
                var has_data = false;
                Object.keys(args).map(function(k) {
                        if (k[0] === '_') return;
                        form_data.append(k, args[k]);
                        has_data = true;
                });

                if (has_data) {
                        req.send(form_data);
                } else {
                        req.send();
                }
        }
})();</script>

						
	
		<script>
			if (window.location.host == 'slack.com' && window.location.search.indexOf('story') < 0) {
				document.cookie = '__cvo_skip_doc=' + escape(document.URL) + '|' + escape(document.referrer) + ';path=/';
			}
		</script>
	

	
		<script type="text/javascript">
		
		try {
			if(window.location.hash && !window.location.hash.match(/^(#?[a-zA-Z0-9_]*)$/)) {
				window.location.hash = '';
			}
		} catch(e) {}
		
	</script>

	<script type="text/javascript">
				(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
		ga('create', "UA-106458-17", 'slack.com');

				
		ga('send', 'pageview');
	
		(function(e,c,b,f,d,g,a){e.SlackBeaconObject=d;
		e[d]=e[d]||function(){(e[d].q=e[d].q||[]).push([1*new Date(),arguments])};
		e[d].l=1*new Date();g=c.createElement(b);a=c.getElementsByTagName(b)[0];
		g.async=1;g.src=f;a.parentNode.insertBefore(g,a)
		})(window,document,"script","https://a.slack-edge.com/dcf8/js/libs/beacon.js","sb");
		sb('set', 'token', '3307f436963e02d4f9eb85ce5159744c');

					sb('set', 'user_id', "U2J9JLDBQ");
							sb('set', 'user_' + "batch", "signup_api");
							sb('set', 'user_' + "created", "2016-10-01");
						sb('set', 'name_tag', "hackathonnetwork" + '/' + "kmr");
				sb('track', 'pageview');

		function track(a){ga('send','event','web',a);sb('track',a);}

	</script>



<script type='text/javascript'>
	
	/* safety stub */
	window.mixpanel = {
		track: function() {},
		track_links: function() {},
		track_forms: function() {}
	};

	function mixpanel_track(){}
	function mixpanel_track_forms(){}
	function mixpanel_track_links(){}
	
</script>
	
	<meta name="referrer" content="no-referrer">
		<meta name="superfish" content="nofish">

	<script type="text/javascript">



var TS_last_log_date = null;
var TSMakeLogDate = function() {
	var date = new Date();

	var y = date.getFullYear();
	var mo = date.getMonth()+1;
	var d = date.getDate();

	var time = {
	  h: date.getHours(),
	  mi: date.getMinutes(),
	  s: date.getSeconds(),
	  ms: date.getMilliseconds()
	};

	Object.keys(time).map(function(moment, index) {
		if (moment == 'ms') {
			if (time[moment] < 10) {
				time[moment] = time[moment]+'00';
			} else if (time[moment] < 100) {
				time[moment] = time[moment]+'0';
			}
		} else if (time[moment] < 10) {
			time[moment] = '0' + time[moment];
		}
	});

	var str = y + '/' + mo + '/' + d + ' ' + time.h + ':' + time.mi + ':' + time.s + '.' + time.ms;
	if (TS_last_log_date) {
		var diff = date-TS_last_log_date;
		//str+= ' ('+diff+'ms)';
	}
	TS_last_log_date = date;
	return str+' ';
}

var parseDeepLinkRequest = function(code) {
	var m = code.match(/"id":"([CDG][A-Z0-9]{8})"/);
	var id = m ? m[1] : null;

	m = code.match(/"team":"(T[A-Z0-9]{8})"/);
	var team = m ? m[1] : null;

	m = code.match(/"message":"([0-9]+\.[0-9]+)"/);
	var message = m ? m[1] : null;

	return { id: id, team: team, message: message };
}

if ('rendererEvalAsync' in window) {
	var origRendererEvalAsync = window.rendererEvalAsync;
	window.rendererEvalAsync = function(blob) {
		try {
			var data = JSON.parse(decodeURIComponent(atob(blob)));
			if (data.code.match(/handleDeepLink/)) {
				var request = parseDeepLinkRequest(data.code);
				if (!request.id || !request.team || !request.message) return;

				request.cmd = 'channel';
				TSSSB.handleDeepLinkWithArgs(JSON.stringify(request));
				return;
			} else {
				origRendererEvalAsync(blob);
			}
		} catch (e) {
		}
	}
}
</script>



<script type="text/javascript">

	var TSSSB = {
		call: function() {
			return false;
		}
	};

</script>
<script>TSSSB.env = (function() {
	'use strict';

	var v = {
		win_ssb_version: null,
		win_ssb_version_minor: null,
		mac_ssb_version: null,
		mac_ssb_version_minor: null,
		mac_ssb_build: null,
		lin_ssb_version: null,
		lin_ssb_version_minor: null,
		desktop_app_version: null
	};

	var is_win = (navigator.appVersion.indexOf("Windows") !== -1);
	var is_lin = (navigator.appVersion.indexOf("Linux") !== -1);
	var is_mac = !!(navigator.userAgent.match(/(OS X)/g));

	if (navigator.userAgent.match(/(Slack_SSB)/g) || navigator.userAgent.match(/(Slack_WINSSB)/g)) {
		
		var parts = navigator.userAgent.split('/');
		var version_str = parts[parts.length-1];
		var version_float = parseFloat(version_str);
		var version_parts = version_str.split('.');
		var version_minor = (version_parts.length == 3) ? parseInt(version_parts[2]) : 0;

		if (navigator.userAgent.match(/(AtomShell)/g)) {
			
			if (is_lin) {
				v.lin_ssb_version = version_float;
				v.lin_ssb_version_minor = version_minor;
			} else if (is_win) {
				v.win_ssb_version = version_float;
				v.win_ssb_version_minor = version_minor;
			} else if (is_mac) {
				v.mac_ssb_version = version_float;
				v.mac_ssb_version_minor = version_minor;
			}

			if (version_parts.length >= 3) {
				v.desktop_app_version = {
					major: parseInt(version_parts[0]),
					minor: parseInt(version_parts[1]),
					patch: parseInt(version_parts[2])
				}
			}
		} else {
			
			v.mac_ssb_version = version_float;
			v.mac_ssb_version_minor = version_minor;

			
			
			var app_ver = window.macgap && macgap.app && macgap.app.buildVersion && macgap.app.buildVersion();
			var matches = String(app_ver).match(/(?:\()(.*)(?:\))/);
			v.mac_ssb_build = (matches && matches.length == 2) ? parseInt(matches[1] || 0) : 0;
		}
	}

	return v;
})();
</script>


	<script type="text/javascript">
		
		var was_TS = window.TS;
		delete window.TS;
		TSSSB.call('didFinishLoading');
		if (was_TS) window.TS = was_TS;
	</script>
	    <title>Split_task.py | Hackathon Slack</title>
    <meta name="author" content="Slack">

	
		
	
	
					
	
				
	
	
	
	
			<!-- output_css "core" -->
    <link href="https://a.slack-edge.com/21a6/style/rollup-plastic.css" rel="stylesheet" type="text/css" crossorigin="anonymous">

		<!-- output_css "before_file_pages" -->
    <link href="https://a.slack-edge.com/74a30/style/libs/codemirror.css" rel="stylesheet" type="text/css" crossorigin="anonymous">
    <link href="https://a.slack-edge.com/c2a17/style/codemirror_overrides.css" rel="stylesheet" type="text/css" crossorigin="anonymous">

	<!-- output_css "file_pages" -->
    <link href="https://a.slack-edge.com/e542/style/rollup-file_pages.css" rel="stylesheet" type="text/css" crossorigin="anonymous">

	<!-- output_css "regular" -->
    <link href="https://a.slack-edge.com/0dcb2/style/print.css" rel="stylesheet" type="text/css" crossorigin="anonymous">
    <link href="https://a.slack-edge.com/1d9c/style/libs/lato-1-compressed.css" rel="stylesheet" type="text/css" crossorigin="anonymous">

	

	
	
		<meta name="robots" content="noindex, nofollow" />
	

	
<link id="favicon" rel="shortcut icon" href="https://a.slack-edge.com/66f9/img/icons/favicon-32.png" sizes="16x16 32x32 48x48" type="image/png" />

<link rel="icon" href="https://a.slack-edge.com/0180/img/icons/app-256.png" sizes="256x256" type="image/png" />

<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://a.slack-edge.com/66f9/img/icons/ios-152.png" />
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://a.slack-edge.com/66f9/img/icons/ios-144.png" />
<link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://a.slack-edge.com/66f9/img/icons/ios-120.png" />
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://a.slack-edge.com/66f9/img/icons/ios-114.png" />
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://a.slack-edge.com/0180/img/icons/ios-72.png" />
<link rel="apple-touch-icon-precomposed" href="https://a.slack-edge.com/66f9/img/icons/ios-57.png" />

<meta name="msapplication-TileColor" content="#FFFFFF" />
<meta name="msapplication-TileImage" content="https://a.slack-edge.com/66f9/img/icons/app-144.png" />
	
	<!--[if lt IE 9]>
	<script src="https://a.slack-edge.com/ef0d/js/libs/html5shiv.js"></script>
	<![endif]-->

</head>

<body class="			">

		  			<script>
		
			var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
			if (w > 1440) document.querySelector('body').classList.add('widescreen');
		
		</script>
	
  	
	

			<nav id="site_nav" class="no_transition">

	<div id="site_nav_contents">

		<div id="user_menu">
			<div id="user_menu_contents">
				<div id="user_menu_avatar">
										<span class="member_image thumb_48" style="background-image: url('https://secure.gravatar.com/avatar/7683c047a1970818fa0e40866216d041.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2F7fa9%2Fimg%2Favatars%2Fava_0011-192.png')" data-thumb-size="48" data-member-id="U2J9JLDBQ"></span>
					<span class="member_image thumb_36" style="background-image: url('https://secure.gravatar.com/avatar/7683c047a1970818fa0e40866216d041.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2F3654%2Fimg%2Favatars%2Fava_0011-72.png')" data-thumb-size="36" data-member-id="U2J9JLDBQ"></span>
				</div>
				<h3>Signed in as</h3>
				<span id="user_menu_name">kmr</span>
			</div>
		</div>

		<div class="nav_contents">

			<ul class="primary_nav">
				<li><a href="/home" data-qa="home"><i class="ts_icon ts_icon_home"></i>Home</a></li>
				<li><a href="/account" data-qa="account_profile"><i class="ts_icon ts_icon_user"></i>Account & Profile</a></li>
				<li><a href="/apps/manage" data-qa="configure_apps" target="_blank"><i class="ts_icon ts_icon_plug"></i>Configure Apps</a></li>
				<li><a href="/archives"data-qa="archives"><i class="ts_icon ts_icon_archive" ></i>Message Archives</a></li>
				<li><a href="/files" data-qa="files"><i class="ts_icon ts_icon_all_files clear_blue"></i>Files</a></li>
				<li><a href="/team" data-qa="team_directory"><i class="ts_icon ts_icon_team_directory"></i>Team Directory</a></li>
									<li><a href="/stats" data-qa="statistics"><i class="ts_icon ts_icon_dashboard"></i>Statistics</a></li>
													<li><a href="/customize" data-qa="customize"><i class="ts_icon ts_icon_magic"></i>Customize</a></li>
											</ul>

							<h3>Administration</h3>
				<ul id="admin_nav" class="secondary_nav">
					<li><a href="/admin/settings" data-qa="team_settings">Settings & Permissions</a></li>
					<li><a href="/admin" data-qa="manage_your_team">Manage Your Team</a></li>
					<li><a href="/admin/invites" data-qa="invitations">Invitations</a></li>
					<li><a href="/admin/billing" data-qa="billing">Billing</a></li>
																	<li><a href="/admin/auth" data-qa="authentication">Authentication</a></li>
									</ul>
			
		</div>

		<div id="footer">

			<ul id="footer_nav">
				<li><a href="/is" data-qa="tour">Tour</a></li>
				<li><a href="/downloads" data-qa="download_apps">Download Apps</a></li>
				<li><a href="/brand-guidelines" data-qa="brand_guidelines">Brand Guidelines</a></li>
				<li><a href="/help" data-qa="help">Help</a></li>
				<li><a href="https://api.slack.com" target="_blank" data-qa="api">API<i class="ts_icon ts_icon_external_link small_left_margin ts_icon_inherit"></i></a></li>
									<li><a href="/account/gateways" data-qa="gateways">Gateways</a></li>
								<li><a href="/pricing" data-qa="pricing">Pricing</a></li>
				<li><a href="/help/requests/new" data-qa="contact">Contact</a></li>
				<li><a href="/terms-of-service" data-qa="policies">Policies</a></li>
				<li><a href="http://slackhq.com/" target="_blank" data-qa="our_blog">Our Blog</a></li>
				<li><a href="https://slack.com/signout/86274076755?crumb=s-1475373670-d27605c588-%E2%98%83" data-qa="sign_out">Sign Out<i class="ts_icon ts_icon_sign_out small_left_margin ts_icon_inherit"></i></a></li>
			</ul>

			<p id="footer_signature">Made with <i class="ts_icon ts_icon_heart"></i> by Slack</p>

		</div>

	</div>
</nav>	
	
			<header>
			<a id="menu_toggle" class="no_transition" data-qa="menu_toggle_hamburger">
			<span class="menu_icon"></span>
			<span class="menu_label">Menu</span>
			<span class="vert_divider"></span>
		</a>
		<h1 id="header_team_name" class="inline_block no_transition" data-qa="header_team_name">
			<a href="/home">
				<i class="ts_icon ts_icon_home" /></i>
				Hackathon
			</a>
		</h1>
		<div class="header_nav">
			<div class="header_btns float_right">
				<a id="team_switcher" data-qa="team_switcher">
					<i class="ts_icon ts_icon_th_large ts_icon_inherit"></i>
					<span class="block label">Teams</span>
				</a>
				<a href="/help" id="help_link" data-qa="help_link">
					<i class="ts_icon ts_icon_life_ring ts_icon_inherit"></i>
					<span class="block label">Help</span>
				</a>
									<a href="/messages" data-qa="launch">
						<img src="https://a.slack-edge.com/66f9/img/icons/ios-64.png" srcset="https://a.slack-edge.com/66f9/img/icons/ios-32.png 1x, https://a.slack-edge.com/66f9/img/icons/ios-64.png 2x" />
						<span class="block label">Launch</span>
					</a>
							</div>
				                    <ul id="header_team_nav" data-qa="team_switcher_menu">
	                        	                            <li class="active">
	                            	<a href="https://hackathonnetwork.slack.com/home" target="https://hackathonnetwork.slack.com/">
	                            			                            			<i class="ts_icon small ts_icon_check_circle_o active_icon s"></i>
	                            			                            			                            			<i class="team_icon small default" >H</i>
	                            			                            		<span class="switcher_label team_name">Hackathon</span>
	                            	</a>
	                            </li>
	                        	                            <li >
	                            	<a href="https://mis17.slack.com/home" target="https://mis17.slack.com/">
	                            			                            			                            			<i class="team_icon small default" style="background: #0D7E83;">TM</i>
	                            			                            		<span class="switcher_label team_name">TAMU MS-MIS Class of &#039;17</span>
	                            	</a>
	                            </li>
	                        	                        <li id="add_team_option"><a href="https://slack.com/signin" target="_blank"><i class="ts_icon ts_icon_plus team_icon small"></i> <span class="switcher_label">Sign in to another team...</span></a></li>
	                    </ul>
	                		</div>
	
	
</header>	
	<div id="page" >

		<div id="page_contents" data-qa="page_contents" class="">

<p class="print_only">
	<strong>Created by varun03 on October 1, 2016 at 8:59 PM</strong><br />
	<span class="subtle_silver break_word">https://hackathonnetwork.slack.com/files/varun03/F2JBMRH0R/split_task.py</span>
</p>

<div class="file_header_container no_print"></div>

<div class="alert_container">
		<div class="file_public_link_shared alert" style="display: none;">
			<a id="file_public_link_revoker" class="btn btn_small btn_outline float_right" data-toggle="tooltip" title="You can revoke the public link to this file. This will cause any previously shared links to stop working.">Revoke</a>
		
	<i class="ts_icon ts_icon_link"></i> Public Link: <a class="file_public_link" href="https://slack-files.com/T2J8228N7-F2JBMRH0R-558586d1a3" target="new">https://slack-files.com/T2J8228N7-F2JBMRH0R-558586d1a3</a>
</div></div>

<div id="file_page" class="card top_padding">

	<p class="small subtle_silver no_print meta">
		11KB Python snippet created on <span class="date">October 1st 2016</span>.
				<span class="file_share_list"></span>
	</p>

	<a id="file_action_cog" class="action_cog action_cog_snippet float_right no_print">
		<span>Actions </span><i class="ts_icon ts_icon_cog"></i>
	</a>
	<a id="snippet_expand_toggle" class="float_right no_print">
		<i class="ts_icon ts_icon_expand "></i>
		<i class="ts_icon ts_icon_compress hidden"></i>
	</a>

	<div class="large_bottom_margin clearfix">
		<pre id="file_contents">from flask import Flask, flash, redirect, render_template,request, url_for, json
from flask.ext.mysql import MySQL
import json
import traceback
import datetime
from datetime import timedelta
app = Flask(__name__)
mysql = MySQL()
app = Flask(__name__)
app.config[&#039;MYSQL_DATABASE_USER&#039;] = &#039;root&#039;
app.config[&#039;MYSQL_DATABASE_PASSWORD&#039;] = &#039;admin&#039;
app.config[&#039;MYSQL_DATABASE_DB&#039;] = &#039;mysql&#039;
app.config[&#039;MYSQL_DATABASE_HOST&#039;] = &#039;localhost&#039;
mysql.init_app(app)
app = Flask(__name__)
app.secret_key = &#039;login_secret&#039; 


# @app.route(&quot;/&quot;)
# def main():
# 	return redirect(url_for(&#039;viewalltasks&#039;))

@app.route(&quot;/addtask&quot;,methods=[&#039;GET&#039;,&#039;POST&#039;])
def addtask():
	#json_data_add = &#039;{&quot;login_id&quot;: 1, &quot;task_name&quot;: &quot;HEB&quot;,&quot;start_date&quot;:&quot;2015-09-01&quot;,&quot;end_date&quot;:&quot;2015-09-30&quot;, &quot;frequency&quot;:&quot;Daily&quot;,&quot;participants&quot;:[1,2,3,4],&quot;multiple&quot;:1}&#039;
	print (&quot;entered...............................&quot;)
	json_data_add = request.get_json(silent=True)
	print (json_data_add)
	python_obj =json_data_add[1]
	#python_obj = json.loads(str(json_data_add))
	login_id=python_obj[&quot;login_id&quot;]
	task_name=python_obj[&quot;task_name&quot;]
	start_date=python_obj[&quot;start_date&quot;]
	start_date=datetime.datetime.strptime(start_date,&quot;%d/%m/%Y&quot;)
	end_date=python_obj[&quot;end_date&quot;]
	end_date=datetime.datetime.strptime(end_date,&quot;%d/%m/%Y&quot;)
	multiple=python_obj[&quot;multiple&quot;]
	frequency=python_obj[&quot;frequency&quot;]
	if(frequency==&#039;Daily&#039;):
		frequency=1
	if(frequency==&#039;Weekly&#039;):
		frequency=7
	participants=python_obj[&quot;participants&quot;]
	sql=&#039;select uid from split_task.customers_auth where uid in (&#039;
	data = {}
	try:
		conn=mysql.connect()
		cursor = conn.cursor()
		cursor.execute(&#039;&#039;&#039;INSERT into split_task.task_master (TASK_NAME) values (%s)&#039;&#039;&#039;, (task_name))
		for p in participants:
			cursor.execute(&#039;&#039;&#039;INSERT into split_task.task_list (TASK_ID,GROUP_ID,FREQUENCY,START_DATE,END_DATE,LOGIN_ID,CREATED_BY,STATUS,MULTIPLE) values ((select TASK_ID from split_task.task_master where TASK_NAME=%s),(select group_id from split_task.customers_auth where uid=%s),%s,%s,%s,%s,%s,%s,%s)&#039;&#039;&#039;, (task_name,login_id,frequency,start_date,end_date,p,login_id,&#039;ACTIVE&#039;,multiple))
			sql=sql+str(p)+&quot;,&quot;
		sql = sql[:-1]
			
		sql=sql+&#039;) order by name &#039;
		
		cursor.execute(sql)
		rows = cursor.fetchall()
		i=0
		k=0
		due_date=start_date
		list_alphabetical = list()
		for row in rows:
			list_alphabetical.append(row[0])
		flag_second_due=False
		flag_first_due_done=False
		
		while (end_date&gt;=due_date):
			due_date=start_date+ timedelta(days=i)
			i=i+int(frequency)	
			flag_dontrun=False
			# Get task assigned for the due date in order and take the next user and then keep assigning alphabetically
			index_last_user=0		
			if(flag_second_due!=True):
				cursor.execute(&#039;&#039;&#039;select login_id from split_task.task_status where due_date=%s and pk_ts=(select max(pk_ts) from split_task.task_status where due_date=%s) &#039;&#039;&#039; , (due_date,due_date))
				rows = cursor.fetchall()
				for row in rows:
					flag_first_due_done=True
					flag_second_due=True
					index_last_user=list_alphabetical.index(row[0])
					#print (index_last_user,list_alphabetical)
					if((index_last_user+1)&lt; len(list_alphabetical)):
						next_user_index=index_last_user+1
					else:
						next_user_index=0
					for j in range(multiple):
						
						cursor.execute(&#039;&#039;&#039;INSERT INTO split_task.task_status  (TASK_ID,DUE_DATE,LOGIN_ID,STATUS) VALUES ((select TASK_ID from split_task.task_master where TASK_NAME=%s),%s,%s,%s)&#039;&#039;&#039;, (task_name,due_date,list_alphabetical[next_user_index],&#039;Pending&#039;))
						if((next_user_index)&lt;len(list_alphabetical)-1):
							k=next_user_index+1
						else:
							k=0
						next_user_index=k
					flag_dontrun=True
					
			
			if(flag_first_due_done==False or flag_second_due==True and flag_dontrun==False):
				#If no task assigned use the alphabetical name
				flag_second_due=True
				for j in range(multiple):
					cursor.execute(&#039;&#039;&#039;INSERT INTO split_task.task_status  (TASK_ID,DUE_DATE,LOGIN_ID,STATUS) VALUES ((select TASK_ID from split_task.task_master where TASK_NAME=%s),%s,%s,%s)&#039;&#039;&#039;, (task_name,due_date,list_alphabetical[k],&#039;Pending&#039;))
					if(k&lt;len(list_alphabetical)-1):
						k=k+1
					else:
						k=0
		
		data[&#039;key&#039;] = &quot;Success&quot;
		json_data = json.dumps(data)	
		conn.commit()
	except:
	
		data[&#039;key&#039;] = &quot;Failed&quot;	
		json_data = json.dumps(data)	
		traceback.print_exc()
		print (&quot;failed insertion in task_master&quot;)
		conn.rollback()
	conn.close()
	print (&#039;JSON: &#039;, json_data)
	return json_data

@app.route(&quot;/viewallhometasks&quot;,methods=[&#039;GET&#039;,&#039;POST&#039;])
def viewallhometasks():

	json_data_view = request.get_json(silent=True)
	json_data_view=json.dumps(json_data_view, ensure_ascii=False)
	#json_data_view=&#039;{&quot;uid&quot;: 1}&#039;
	print(json_data_view)
	container={}
	final=[]
	data = {}
	try:
		
		python_obj = json.loads(json_data_view)
		uid=python_obj[&quot;uid&quot;]
		conn=mysql.connect()
		cursor1 = conn.cursor()
		cursor = conn.cursor()
		sql1=&#039;&#039;&#039;SELECT distinct TL.task_id,TM.task_name,TL.start_date,TL.end_date, TL.frequency, TL.MULTIPLE FROM split_task.task_list TL,  split_task.task_master TM  where TL.group_id =(select group_id from split_task.customers_auth where uid=%s)  and TL.task_id=TM.task_id  and TL.status=&#039;ACTIVE&#039; order by TL.TASK_ID desc&#039;&#039;&#039;
		cursor1.execute(sql1, (uid))
		rows = cursor1.fetchall()
		for row in rows:
			item_dict=dict()
			item_dict[&#039;moduleid&#039;] = row[0]
			item_dict[&#039;module&#039;] = row[1]
			item_dict[&#039;startdate&#039;] = row[2].strftime(&quot;%d/%m/%Y&quot;)
			item_dict[&#039;enddate&#039;] = row[3].strftime(&quot;%d/%m/%Y&quot;)
			
			item_dict[&#039;frequency&#039;] = row[4]
			if(item_dict[&#039;frequency&#039;]==1):
				item_dict[&#039;frequency&#039;]=&#039;Daily&#039;
			elif(item_dict[&#039;frequency&#039;]==7):
				item_dict[&#039;frequency&#039;]=&#039;Weekly&#039;
			item_dict[&#039;multiple&#039;] = row[5]


			sql=&#039;&#039;&#039;select lm.uid,lm.name from split_task.customers_auth lm, split_task.task_list tl where tl.login_id=lm.uid and task_id=%s&#039;&#039;&#039;
			cursor.execute(sql, (row[0]))
			rows_users = cursor.fetchall()
			l=list()
			for row in rows_users:
				l.append({&quot;id&quot;:row[0],&quot;name&quot;:row[1]})
			item_dict[&#039;users&#039;] = l

			#container[row[0]] = item_dict
			final.append(item_dict)
		print(final)
		json_data = json.dumps(final)
		conn.commit()
	except:
		traceback.print_exc()
		data[&#039;key&#039;] = &quot;Failed&quot;
		json_data = json.dumps(data)
		print (&quot;failed selection of data&quot;)
		conn.rollback()
	conn.close()
	
	return json_data



def viewallhometasksafterdel(json_data_view):
	
	container={}
	final=[]
	data = {}
	try:	
		python_obj = json.loads(json_data_view)
		group_id=python_obj[&quot;group_id&quot;]
		conn=mysql.connect()
		cursor = conn.cursor()
		sql=&#039;&#039;&#039;SELECT distinct TL.task_id,TM.task_name,TL.start_date,TL.end_date,groupids, TL.frequency, TL.MULTIPLE FROM split_task.task_list TL,  split_task.task_master TM , split_task.customers_auth LM, (select GROUP_CONCAT(lm.name) as groupids,tl.task_id  from split_task.task_list tl,   split_task.customers_auth lm where LM.uid=TL.login_id group by tl.task_id ) subq where TL.group_id =%s and TL.task_id=TM.task_id and LM.uid=TL.login_id and subq.task_id= tl.task_id and TM.status=&#039;ACTIVE&#039; order by TL.TASK_ID desc&#039;&#039;&#039;
		cursor.execute(sql, (group_id))
		rows = cursor.fetchall()
		for row in rows:
			item_dict=dict()
			item_dict[&#039;taskid&#039;] = row[0]
			item_dict[&#039;taskname&#039;] = row[1]
			item_dict[&#039;startdate&#039;] = row[2].strftime(&quot;%d/%m/%Y&quot;)
			item_dict[&#039;end_date&#039;] = row[3].strftime(&quot;%d/%m/%Y&quot;)
			item_dict[&#039;groupids&#039;] = row[4]
			item_dict[&#039;frequency&#039;] = row[5]
			if(item_dict[&#039;frequency&#039;]==1):
				item_dict[&#039;frequency&#039;]=&#039;Daily&#039;
			elif(item_dict[&#039;frequency&#039;]==7):
				item_dict[&#039;frequency&#039;]=&#039;Weekly&#039;
			item_dict[&#039;multiple&#039;] = row[6]
			#container[row[0]] = item_dict
			final.append(item_dict)
		print(final)
		json_data = json.dumps(final)
		conn.commit()
	except:
		traceback.print_exc()
		data[&#039;key&#039;] = &quot;Failed&quot;
		json_data = json.dumps(data)
		print (&quot;failed selection of data&quot;)
		conn.rollback()
	conn.close()
	
	return json_data

	   
@app.route(&quot;/deletehometask&quot;,methods=[&#039;GET&#039;,&#039;POST&#039;])
def deletehometask():
	json_data_del = &#039;{&quot;task_id&quot;: 62,&quot;group_id&quot;: 134}&#039;
	#json_data_del = request.get_json(silent=True)
	python_obj = json.loads(json_data_del)
	task_id=python_obj[&quot;task_id&quot;]
	data = {}
	try:
		conn=mysql.connect()
		cursor = conn.cursor()
		cursor.execute(&#039;&#039;&#039;delete from  split_task.task_list  where task_id=%s&#039;&#039;&#039;, (task_id))
		cursor.execute(&#039;&#039;&#039;delete from  split_task.task_status  where task_id=%s and due_date&gt; now()&#039;&#039;&#039;, (task_id))
		cursor.execute(&#039;&#039;&#039;delete from  split_task.task_master  where task_id=%s&#039;&#039;&#039;, (task_id))
		conn.commit()
	except:
	
		data[&#039;key&#039;] = &quot;Failed&quot;	
		json_data = json.dumps(data)	
		traceback.print_exc()
		print (&quot;failed insertion in task_master&quot;)
		conn.rollback()
		return json_data
	json_data=viewallhometasksafterdel(json_data_del)
	print (&#039;JSON: &#039;, json_data)
	return json_data


@app.route(&quot;/viewalltasks&quot;,methods=[&#039;GET&#039;,&#039;POST&#039;])
def viewalltasks():
	#json_data_view = request.get_json(silent=True)
	json_data_view=&#039;{&quot;due_date&quot;: &quot;12/09/2015&quot;,&quot;uid&quot;: 1}&#039;
	container={}
	final=[]
	data = {}
	try:
		
		python_obj = json.loads(json_data_view)
		due_date=python_obj[&quot;due_date&quot;]
		due_date=datetime.datetime.strptime(due_date,&quot;%d/%m/%Y&quot;)
		uid=python_obj[&quot;uid&quot;]
		conn=mysql.connect()
		cursor = conn.cursor()
		sql=&#039;&#039;&#039;select tm.task_id,task_name,ts.due_date,ts.status from split_task.task_status ts,  split_task.task_master tm where  login_id=%s and due_date=%s and tm.task_id=ts.task_id order by TS.TASK_ID desc&#039;&#039;&#039;
		print(sql,due_date)
		cursor.execute(sql, (uid,due_date))
		rows = cursor.fetchall()
		for row in rows:
			item_dict=dict()
			item_dict[&#039;taskid&#039;] = row[0]
			item_dict[&#039;taskname&#039;] = row[1]
			item_dict[&#039;duedate&#039;] = row[2].strftime(&quot;%d/%m/%Y&quot;)
			#container[row[0]] = item_dict
			final.append(item_dict)
		print(final)
		json_data = json.dumps(final)
		conn.commit()
	except:
		traceback.print_exc()
		data[&#039;key&#039;] = &quot;Failed&quot;
		json_data = json.dumps(data)
		print (&quot;failed selection of data&quot;)
		conn.rollback()
	conn.close()
	
	return json_data
	

@app.route(&quot;/updatecompletion&quot;,methods=[&#039;GET&#039;,&#039;POST&#039;])
def updatecompletion():
	json_data_upd = &#039;{&quot;task_id&quot;: 59,&quot;uid&quot;: 1,&quot;status&quot;: &quot;Completed&quot;}&#039;
	#json_data_upd = request.get_json(silent=True)
	python_obj = json.loads(json_data_upd)
	task_id=python_obj[&quot;task_id&quot;]
	uid=python_obj[&quot;uid&quot;]
	status=python_obj[&quot;status&quot;]
	data = {}
	try:
		conn=mysql.connect()
		cursor = conn.cursor()
		cursor.execute(&#039;&#039;&#039;update split_task.task_status set status=%s where task_id=%s and login_id=%s&#039;&#039;&#039;, (status,task_id,uid))
		conn.commit()
		data[&#039;key&#039;] = &quot;Success&quot;	
		json_data = json.dumps(data)	
	except:
	
		data[&#039;key&#039;] = &quot;Failed&quot;	
		json_data = json.dumps(data)	
		traceback.print_exc()
		print (&quot;failed update in task_master&quot;)
		conn.rollback()
	
	return json_data

if __name__ == &quot;__main__&quot;:
    app.run()
</pre>

		<p class="file_page_meta no_print" style="line-height: 1.5rem;">
			<label class="checkbox normal mini float_right no_top_padding no_min_width">
				<input type="checkbox" id="file_preview_wrap_cb"> wrap long lines
			</label>
		</p>

	</div>

	<div id="comments_holder" class="clearfix clear_both">
	<div class="col span_1_of_6"></div>
	<div class="col span_4_of_6 no_right_padding">
		<div id="file_page_comments">
					</div>	
		<form action="https://hackathonnetwork.slack.com/files/varun03/F2JBMRH0R/split_task.py"
		id="file_comment_form"
					class="comment_form"
				method="post">
			<a href="/team/kmr" class="member_preview_link" data-member-id="U2J9JLDBQ" >
			<span class="member_image thumb_36" style="background-image: url('https://secure.gravatar.com/avatar/7683c047a1970818fa0e40866216d041.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2F3654%2Fimg%2Favatars%2Fava_0011-72.png')" data-thumb-size="36" data-member-id="U2J9JLDBQ"></span>
		</a>
		<input type="hidden" name="addcomment" value="1" />
	<input type="hidden" name="crumb" value="s-1475373670-d8e3cb8662-☃" />

	<textarea id="file_comment" data-el-id-to-keep-in-view="file_comment_submit_btn" class="small comment_input small_bottom_margin autogrow-short" name="comment" wrap="virtual" ></textarea>
	<span class="input_note float_left cloud_silver file_comment_tip">shift+enter to add a new line</span>	<button id="file_comment_submit_btn" type="submit" class="btn float_right  ladda-button" data-style="expand-right"><span class="ladda-label">Add Comment</span></button>
</form>

<form
		id="file_edit_comment_form"
					class="edit_comment_form hidden"
				method="post">
		<textarea id="file_edit_comment" class="small comment_input small_bottom_margin" name="comment" wrap="virtual"></textarea><br>
	<span class="input_note float_left cloud_silver file_comment_tip">shift+enter to add a new line</span>	<input type="submit" class="save btn float_right " value="Save" />
	<button class="cancel btn btn_outline float_right small_right_margin ">Cancel</button>
</form>	
	</div>
	<div class="col span_1_of_6"></div>
</div>
</div>



		
	</div>
	<div id="overlay"></div>
</div>







<script type="text/javascript">

	function vvv(v) {

		var vvv_warning = 'You cannot use vvv on dynamic values. Please make sure you only pass in static file paths.';
		if (TS && TS.warn) {
			TS.warn(vvv_warning);
		} else {
			console.warn(vvv_warning);
		}

		return v;
	}

	var cdn_url = "https:\/\/slack.global.ssl.fastly.net";
	var inc_js_setup_data = {
		emoji_sheets: {
			apple: 'https://a.slack-edge.com/f360/img/emoji_2016_06_08/sheet_apple_64_indexed_256colors.png',
			google: 'https://a.slack-edge.com/f360/img/emoji_2016_06_08/sheet_google_64_indexed_128colors.png',
			twitter: 'https://a.slack-edge.com/f360/img/emoji_2016_06_08/sheet_twitter_64_indexed_128colors.png',
			emojione: 'https://a.slack-edge.com/f360/img/emoji_2016_06_08/sheet_emojione_64_indexed_128colors.png',
		},
	};
</script>
			<script type="text/javascript">
<!--
	// common boot_data
	var boot_data = {
		start_ms: Date.now(),
		app: 'web',
		user_id: 'U2J9JLDBQ',
		no_login: false,
		version_ts: '1475282541',
		version_uid: '795747d2348f6076ea22c1c5b15541a198621ba2',
		cache_version: "v13-tiger",
		cache_ts_version: "v1-cat",
		redir_domain: 'slack-redir.net',
		signin_url: 'https://slack.com/signin',
		abs_root_url: 'https://slack.com/',
		api_url: '/api/',
		team_url: 'https://hackathonnetwork.slack.com/',
		image_proxy_url: 'https://slack-imgs.com/',
		beacon_timing_url: "https:\/\/slack.com\/beacon\/timing",
		beacon_error_url: "https:\/\/slack.com\/beacon\/error",
		clog_url: "clog\/track\/",
		api_token: 'xoxs-86274076755-86324693398-86334991143-33d00bdd78',
		ls_disabled: false,

		notification_sounds: [{"value":"b2.mp3","label":"Ding","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/b2.mp3"},{"value":"animal_stick.mp3","label":"Boing","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/animal_stick.mp3"},{"value":"been_tree.mp3","label":"Drop","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/been_tree.mp3"},{"value":"complete_quest_requirement.mp3","label":"Ta-da","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/complete_quest_requirement.mp3"},{"value":"confirm_delivery.mp3","label":"Plink","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/confirm_delivery.mp3"},{"value":"flitterbug.mp3","label":"Wow","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/flitterbug.mp3"},{"value":"here_you_go_lighter.mp3","label":"Here you go","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/here_you_go_lighter.mp3"},{"value":"hi_flowers_hit.mp3","label":"Hi","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/hi_flowers_hit.mp3"},{"value":"item_pickup.mp3","label":"Yoink","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/item_pickup.mp3"},{"value":"knock_brush.mp3","label":"Knock Brush","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/knock_brush.mp3"},{"value":"save_and_checkout.mp3","label":"Woah!","url":"https:\/\/slack.global.ssl.fastly.net\/dfc0\/sounds\/push\/save_and_checkout.mp3"},{"value":"none","label":"None"}],
		alert_sounds: [{"value":"frog.mp3","label":"Frog","url":"https:\/\/slack.global.ssl.fastly.net\/a34a\/sounds\/frog.mp3"}],
		call_sounds: [{"value":"call\/alert_v2.mp3","label":"Alert","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/alert_v2.mp3"},{"value":"call\/incoming_ring_v2.mp3","label":"Incoming ring","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/incoming_ring_v2.mp3"},{"value":"call\/outgoing_ring_v2.mp3","label":"Outgoing ring","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/outgoing_ring_v2.mp3"},{"value":"call\/pop_v2.mp3","label":"Incoming reaction","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/pop_v2.mp3"},{"value":"call\/they_left_call_v2.mp3","label":"They left call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/they_left_call_v2.mp3"},{"value":"call\/you_left_call_v2.mp3","label":"You left call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/you_left_call_v2.mp3"},{"value":"call\/they_joined_call_v2.mp3","label":"They joined call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/they_joined_call_v2.mp3"},{"value":"call\/you_joined_call_v2.mp3","label":"You joined call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/you_joined_call_v2.mp3"},{"value":"call\/confirmation_v2.mp3","label":"Confirmation","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/confirmation_v2.mp3"}],
		call_sounds_version: "v2",
		max_team_handy_rxns: 5,
		max_channel_handy_rxns: 5,
		max_poll_handy_rxns: 7,
		max_handy_rxns_title_chars: 30,
		
		feature_tinyspeck: false,
		feature_i18n: false,
		feature_create_team_google_auth: false,
		feature_api_extended_2fa_backup: false,
		feature_flannel_fe: false,
		feature_ts_ms_refactor: true,
		feature_emoji_usage_stats: false,
		feature_viewmodel_proto: false,
		feature_sales_tax: false,
		feature_message_replies: false,
		feature_message_replies_rewrite_864: false,
		feature_message_replies_off: false,
		feature_no_rollups: false,
		feature_web_lean: false,
		feature_web_lean_all_users: false,
		feature_reminders_v3: true,
		feature_all_skin_tones: false,
		feature_server_side_emoji_counts: true,
		feature_a11y_keyboard_shortcuts: false,
		feature_email_ingestion: false,
		feature_msg_consistency: false,
		feature_sli_channel_priority: false,
		feature_sli_similar_channels: true,
		feature_sli_channel_suggestbot: true,
		feature_sli_clog_selections: false,
		feature_emoji_keywords: true,
		feature_thanks: false,
		feature_attachments_inline: false,
		feature_fix_files: true,
		feature_files_list: true,
		feature_channel_eventlog_client: true,
		feature_macssb1_banner: true,
		feature_macssb2_banner: true,
		feature_latest_event_ts: true,
		feature_elide_closed_dms: true,
		feature_no_redirects_in_ssb: true,
		feature_referer_policy: true,
		feature_more_field_in_message_attachments: false,
		feature_calls: true,
		feature_calls_no_rtm_start: true,
		feature_integrations_message_preview: true,
		feature_paging_api: false,
		feature_enterprise_api: true,
		feature_enterprise_create: true,
		feature_enterprise_api_auth: true,
		feature_enterprise_profile: true,
		feature_enterprise_search: true,
		feature_enterprise_team_invite: true,
		feature_enterprise_locked_settings: false,
		feature_frecency_migration: false,
		feature_enterprise_frecency: false,
		feature_enterprise_team_overview_page: false,
		feature_enterprise_search_ui: false,
		feature_enterprise_mandatory_2fa: true,
		feature_enterprise_user_account_settings: true,
		feature_enterprise_security_auth_refactor: false,
		feature_enterprise_member_profile_refactor: false,
		feature_private_channels: true,
		feature_mpim_restrictions: false,
		feature_subteams_hard_delete: false,
		feature_no_unread_counts: true,
		feature_js_raf_queue: false,
		feature_shared_channels: false,
		feature_external_shared_channels_ui: false,
		feature_not_a_member_yet_sharing: false,
		feature_allow_shared_general: false,
		feature_manage_shared_channel_teams: false,
		feature_shared_channels_settings: false,
		feature_fast_files_flexpane: true,
		feature_no_has_files: true,
		feature_custom_saml_signin_button_label: true,
		feature_optimistic_im_close: true,
		feature_file_reactions_activity: false,
		feature_admin_approved_apps: true,
		feature_winssb_beta_channel: false,
		feature_inline_media_playback: true,
		feature_branch_io_deeplink: true,
		feature_clog_whats_new: true,
		feature_presence_sub: false,
		feature_live_support_free_plan: false,
		feature_dm_yahself: true,
		feature_slackbot_goes_to_college: false,
		feature_shared_invites: true,
		feature_lato_2_ssb: true,
		feature_refactor_buildmsghtml: false,
		feature_allow_cdn_experiments: false,
		feature_omit_localstorage_users_bots: false,
		feature_disable_ls_compression: false,
		feature_force_ls_compression: false,
		feature_sign_in_with_slack: true,
		feature_sign_in_with_slack_ui_elements: true,
		feature_prevent_msg_rebuild: false,
		feature_app_review_scope_error: true,
		feature_name_tagging_client: false,
		feature_name_tagging_client_extras: false,
		feature_name_tagging_client_search: false,
		feature_msg_input_contenteditable: false,
		feature_browse_date: true,
		feature_use_imgproxy_resizing: false,
		feature_multiple_app_ownership: false,
		feature_update_message_file: true,
		feature_custom_clogs: true,
		feature_channels_view_introspect_messages: true,
		feature_calls_linux: true,
		feature_emoji_hover_styles: true,
		feature_emoji_speed: false,
		feature_a11y_pref_text_size: false,
		feature_a11y_pref_no_animation: false,
		feature_share_mention_comment_cleanup: false,
		feature_unread_view: true,
		feature_unread_view_onboarding: true,
		feature_unread_view_keyboard_commands: false,
		feature_tw: false,
		feature_tw_ls_disabled: false,
		feature_external_files: false,
		feature_min_web: false,
		feature_electron_memory_logging: false,
		feature_channel_name_menu: true,
		feature_electron_window_gripper: true,
		feature_simple_file_events: true,
		feature_devrel_try_it_now: false,
		feature_wait_for_all_mentions_in_client: false,
		feature_free_inactive_domains: true,
		feature_invitebulk_method_in_modal: false,
		feature_invite_modal_contacts: false,
		feature_platform_calls: true,
		feature_a11y_tab: false,
		feature_admin_billing_refactor: false,
		feature_wrapped_mention_parsing: false,
		feature_measure_css_usage: false,
		feature_show_enterprise_signout_all: false,
		feature_enterprise_full_member_invites: false,
		feature_take_profile_photo: false,
		feature_ajax_billing_history: false,
		feature_update_coachmarks_cta: true,
		feature_multnomah: false,
		feature_sales_tax_address: true,
		feature_toggle_id_translation: false,
		feature_can_edit_app: true,
		feature_gdrive_1_dot_5: false,
		feature_hide_email_pref: true,
		feature_ent_pricing_lp: true,
		feature_file_id_from_url_update: false,
		feature_channel_header_refactor: false,
		feature_pin_update: false,
		feature_opt_click_all_unreads: false,

		img: {
			app_icon: 'https://a.slack-edge.com/272a/img/slack_growl_icon.png'
		},
		page_needs_custom_emoji: false,
		page_needs_team_profile_fields: false,
		page_needs_enterprise: false,
		slackbot_help_enabled: true
	};

	
	
	
	
	// client boot data
	
	
	
//-->
</script>	
	
					<!-- output_js "core" -->
<script type="text/javascript" src="https://a.slack-edge.com/4262/js/rollup-core_required_libs.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://a.slack-edge.com/92a0d/js/rollup-core_required_ts.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://a.slack-edge.com/24339/js/TS.web.js" crossorigin="anonymous"></script>

		<!-- output_js "core_web" -->
<script type="text/javascript" src="https://a.slack-edge.com/125e0/js/rollup-core_web.js" crossorigin="anonymous"></script>

		<!-- output_js "secondary" -->
<script type="text/javascript" src="https://a.slack-edge.com/a1896/js/rollup-secondary_a_required.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bebc/js/rollup-secondary_b_required.js" crossorigin="anonymous"></script>

					
	<!-- output_js "regular" -->
<script type="text/javascript" src="https://a.slack-edge.com/eed7/js/TS.web.comments.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://a.slack-edge.com/99f3/js/TS.web.file.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://a.slack-edge.com/cb0fd/js/libs/codemirror.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://a.slack-edge.com/db4a/js/codemirror_load.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://a.slack-edge.com/dfe2/js/TS.ms.js" crossorigin="anonymous"></script>

		<script type="text/javascript">
	<!--
		boot_data.page_needs_custom_emoji = true;

		boot_data.file = {"id":"F2JBMRH0R","created":1475373598,"timestamp":1475373598,"name":"Split_task.py","title":"Split_task.py","mimetype":"text\/plain","filetype":"python","pretty_type":"Python","user":"U2JA6MGPR","editable":true,"size":11010,"mode":"snippet","is_external":false,"external_type":"","is_public":true,"public_url_shared":false,"display_as_bot":false,"username":"","url_private":"https:\/\/files.slack.com\/files-pri\/T2J8228N7-F2JBMRH0R\/split_task.py","url_private_download":"https:\/\/files.slack.com\/files-pri\/T2J8228N7-F2JBMRH0R\/download\/split_task.py","permalink":"https:\/\/hackathonnetwork.slack.com\/files\/varun03\/F2JBMRH0R\/split_task.py","permalink_public":"https:\/\/slack-files.com\/T2J8228N7-F2JBMRH0R-558586d1a3","edit_link":"https:\/\/hackathonnetwork.slack.com\/files\/varun03\/F2JBMRH0R\/split_task.py\/edit","preview":"from flask import Flask, flash, redirect, render_template,request, url_for, json\r\nfrom flask.ext.mysql import MySQL\r\nimport json\r\nimport traceback\r\nimport datetime\r","preview_highlight":"\u003Cdiv class=\"CodeMirror cm-s-default CodeMirrorServer\" oncopy=\"if(event.clipboardData){event.clipboardData.setData('text\/plain',window.getSelection().toString().replace(\/\\u200b\/g,''));event.preventDefault();event.stopPropagation();}\"\u003E\n\u003Cdiv class=\"CodeMirror-code\"\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Efrom\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Eflask\u003C\/span\u003E \u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003EFlask\u003C\/span\u003E, \u003Cspan class=\"cm-variable\"\u003Eflash\u003C\/span\u003E, \u003Cspan class=\"cm-variable\"\u003Eredirect\u003C\/span\u003E, \u003Cspan class=\"cm-variable\"\u003Erender_template\u003C\/span\u003E,\u003Cspan class=\"cm-variable\"\u003Erequest\u003C\/span\u003E, \u003Cspan class=\"cm-variable\"\u003Eurl_for\u003C\/span\u003E, \u003Cspan class=\"cm-variable\"\u003Ejson\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Efrom\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Eflask\u003C\/span\u003E.\u003Cspan class=\"cm-property\"\u003Eext\u003C\/span\u003E.\u003Cspan class=\"cm-property\"\u003Emysql\u003C\/span\u003E \u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003EMySQL\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Ejson\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Etraceback\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Edatetime\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003C\/div\u003E\n\u003C\/div\u003E\n","lines":318,"lines_more":313,"preview_is_truncated":true,"channels":["C2J8229T5"],"groups":[],"ims":[],"comments_count":0};
		boot_data.file.comments = [];

		

		var g_editor;

		$(function(){

			var wrap_long_lines = !!TS.model.code_wrap_long_lines;

			g_editor = CodeMirror(function(elt){
				var content = document.getElementById("file_contents");
				content.parentNode.replaceChild(elt, content);
			}, {
				value: $('#file_contents').text(),
				lineNumbers: true,
				matchBrackets: true,
				indentUnit: 4,
				indentWithTabs: true,
				enterMode: "keep",
				tabMode: "shift",
				viewportMargin: 10,
				readOnly: true,
				lineWrapping: wrap_long_lines
			});

			// past a certain point, CodeMirror rendering may simply stop working.
			// start having CodeMirror use its Long List View-style scolling at >= max_lines.
			var max_lines = 8192;

			var snippet_lines;

			// determine # of lines, limit height accordingly
			if (g_editor.doc && g_editor.doc.lineCount) {
				snippet_lines = parseInt(g_editor.doc.lineCount());
				var new_height;
				if (snippet_lines) {
					// we want the CodeMirror container to collapse around short snippets.
					// however, we want to let it auto-expand only up to a limit, at which point
					// we specify a fixed height so CM can display huge snippets without dying.
					// this is because CodeMirror works nicely with no height set, but doesn't
					// scale (big file performance issue), and doesn't work with min/max-height -
					// so at some point, we have to set an absolute height to kick it into its
					// smart / partial "Long List View"-style rendering mode.
					if (snippet_lines < max_lines) {
						new_height = 'auto';
					} else {
						new_height = (max_lines * 0.875) + 'rem'; // line-to-rem ratio
					}
					var line_count = Math.min(snippet_lines, max_lines);
					TS.info('Applying height of ' + new_height + ' to container for this snippet of ' + snippet_lines + (snippet_lines === 1 ? ' line' : ' lines'));
					$('#page .CodeMirror').height(new_height);
				}
			}

			$('#file_preview_wrap_cb').bind('change', function(e) {
				TS.model.code_wrap_long_lines = $(this).prop('checked');
				g_editor.setOption('lineWrapping', TS.model.code_wrap_long_lines);
			})

			$('#file_preview_wrap_cb').prop('checked', wrap_long_lines);

			CodeMirror.switchSlackMode(g_editor, "python");
		});

		
		$('#file_comment').css('overflow', 'hidden').autogrow();
	//-->
	</script>

			<script type="text/javascript">TS.boot(boot_data);</script>
	
<style>.color_9f69e7:not(.nuc) {color:#9F69E7;}.color_4bbe2e:not(.nuc) {color:#4BBE2E;}.color_e7392d:not(.nuc) {color:#E7392D;}.color_3c989f:not(.nuc) {color:#3C989F;}.color_674b1b:not(.nuc) {color:#674B1B;}.color_e96699:not(.nuc) {color:#E96699;}.color_e0a729:not(.nuc) {color:#E0A729;}.color_684b6c:not(.nuc) {color:#684B6C;}.color_5b89d5:not(.nuc) {color:#5B89D5;}.color_2b6836:not(.nuc) {color:#2B6836;}.color_99a949:not(.nuc) {color:#99A949;}.color_df3dc0:not(.nuc) {color:#DF3DC0;}.color_4cc091:not(.nuc) {color:#4CC091;}.color_9b3b45:not(.nuc) {color:#9B3B45;}.color_d58247:not(.nuc) {color:#D58247;}.color_bb86b7:not(.nuc) {color:#BB86B7;}.color_5a4592:not(.nuc) {color:#5A4592;}.color_db3150:not(.nuc) {color:#DB3150;}.color_235e5b:not(.nuc) {color:#235E5B;}.color_9e3997:not(.nuc) {color:#9E3997;}.color_53b759:not(.nuc) {color:#53B759;}.color_c386df:not(.nuc) {color:#C386DF;}.color_385a86:not(.nuc) {color:#385A86;}.color_a63024:not(.nuc) {color:#A63024;}.color_5870dd:not(.nuc) {color:#5870DD;}.color_ea2977:not(.nuc) {color:#EA2977;}.color_50a0cf:not(.nuc) {color:#50A0CF;}.color_d55aef:not(.nuc) {color:#D55AEF;}.color_d1707d:not(.nuc) {color:#D1707D;}.color_43761b:not(.nuc) {color:#43761B;}.color_e06b56:not(.nuc) {color:#E06B56;}.color_8f4a2b:not(.nuc) {color:#8F4A2B;}.color_902d59:not(.nuc) {color:#902D59;}.color_de5f24:not(.nuc) {color:#DE5F24;}.color_a2a5dc:not(.nuc) {color:#A2A5DC;}.color_827327:not(.nuc) {color:#827327;}.color_3c8c69:not(.nuc) {color:#3C8C69;}.color_8d4b84:not(.nuc) {color:#8D4B84;}.color_84b22f:not(.nuc) {color:#84B22F;}.color_4ec0d6:not(.nuc) {color:#4EC0D6;}.color_e23f99:not(.nuc) {color:#E23F99;}.color_e475df:not(.nuc) {color:#E475DF;}.color_619a4f:not(.nuc) {color:#619A4F;}.color_a72f79:not(.nuc) {color:#A72F79;}.color_7d414c:not(.nuc) {color:#7D414C;}.color_aba727:not(.nuc) {color:#ABA727;}.color_965d1b:not(.nuc) {color:#965D1B;}.color_4d5e26:not(.nuc) {color:#4D5E26;}.color_dd8527:not(.nuc) {color:#DD8527;}.color_bd9336:not(.nuc) {color:#BD9336;}.color_e85d72:not(.nuc) {color:#E85D72;}.color_dc7dbb:not(.nuc) {color:#DC7DBB;}.color_bc3663:not(.nuc) {color:#BC3663;}.color_9d8eee:not(.nuc) {color:#9D8EEE;}.color_8469bc:not(.nuc) {color:#8469BC;}.color_73769d:not(.nuc) {color:#73769D;}.color_b14cbc:not(.nuc) {color:#B14CBC;}</style>

<!-- slack-www-hhvm109 / 2016-10-01 19:01:10 / v795747d2348f6076ea22c1c5b15541a198621ba2 / B:H -->

</body>
</html>