<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'wordpress' );

/** MySQL database password */
define( 'DB_PASSWORD', 'wordpress-pass' );

/** MySQL hostname */
define( 'DB_HOST', 'azeem-a1-t3.cdxhhswkgl8b.us-east-2.rds.amazonaws.com' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'qx5xP.TwtKQ4yBFKi=9W58WtY*9vo( l@omMcsfn{$A8.n+|La^wu),IEr-jR)MM');
define('SECURE_AUTH_KEY',  'aT,It:xiIGd9*/+*!u7F5LWRkv.t5Tm|&=bgS&{KO&,ZZUB4bQ@m<8umr)dROQMC');
define('LOGGED_IN_KEY',    'HJDuGfNwAK;+|u9OBwIc(yA9Q0-L~ Xq&Y7p%t2F,_sU[AA)*<jJG9Pb!IpRZ.*7');
define('NONCE_KEY',        'RKFL(tNJKEXV9PtHKU0@*xk$9fT-|>*Z.v[av6dWZ2caU$u40>C7t:sjNV;ryFtA');
define('AUTH_SALT',        'ZU.^|MiH_9ni}c0y{&%01v-dnNeS1cey$rdqrWS;.}<LJ[@9_[;5>ieCj9+U$ddc');
define('SECURE_AUTH_SALT', 'RoZEnk8F9<LY*?V`Qh~/||Z1YfX@ rJ<x82-KRUS&Vsob/c9-I!*G3PSg}$l+T[*');
define('LOGGED_IN_SALT',   ',zMsd7a*%Q%]ZE}. ^O0S&87.tv0XUHvT(3Pn+T6~~bmAnJ_| -mep<7D;Q-(b`:');
define('NONCE_SALT',       'tkiy0%r+_/1Gyp~a_UT&sqP-vLj2/h:-c,8$yiNA){|i:5x:xf^D_|J98GSy&iU|');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
