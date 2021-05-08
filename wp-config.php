echo "
            <?php

            define( 'DB_NAME', 'wordpress' );

            define( 'DB_USER', 'wordpress' );


            define( 'DB_PASSWORD', 'wordpress-pass' );


            define( 'DB_HOST', 'localhost' );


            define( 'DB_CHARSET', 'utf8' );


            define( 'DB_COLLATE', '' );

            define('AUTH_KEY',         'tDd1StD~*<NL!#<zG=lREYUr,|+US93%[=-.q`uW$.;1BqB6a].3l(okrpadv6vd');
            define('SECURE_AUTH_KEY',  '<P({aIL}N>DnMj$!.Q@R*tw|D5znK&T]}CJKlFf !PeA|vd(+82@t*)|6-O+-t=/');
            define('LOGGED_IN_KEY',    '/RTZMM0Ch}MuNU@^^p )EQ{4S4|]|8!:u<Vzzo>0+ux8vM8*h-gF1hVG^:/,D%I-');
            define('NONCE_KEY',        '0dGB{aK_oXtFdZ/k5,vh_ yIJ.d8LVzFA92AE0J^eoN(o@8i&jdkObdld+8)Hmi$');
            define('AUTH_SALT',        's-P0?&DKy3Qj@-H4-C=,B}rpLa.N?@62>DD5m@!d(~K*4q_hr}j!?Bz4%K#VC&!-');
            define('SECURE_AUTH_SALT', '(oW<IM-%11:ENHZ-LXOw`k(|kBnEX jRRS2RcaL,J,|``Ayrj#=Mzx$lSEcDA$s:');
            define('LOGGED_IN_SALT',   '$!+p3DjA`5,iXK< zq|-Pp&*tvLcDcux3fh=[mI6g+Q=U/!l(_5kgu9~)F(Oa`.U');
            define('NONCE_SALT',       'eO^a<|~GX-~Qoe_9|DDhT3>PVKw_6^:=$H+<Xg+`87^/R}y;[lTR/JCmnV_q-ACa');


            $table_prefix = 'wp_';


            define( 'WP_DEBUG', false );

            if ( ! defined( 'ABSPATH' ) ) {
              define( 'ABSPATH', __DIR__ . '/' );
            }


            require_once ABSPATH . 'wp-settings.php';
            " > wp-config.php
