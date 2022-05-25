from math import pi

def astrConstant(n: int)->float:
    """ astroConstants - Returns astrodynamic-related physical constants.
    
     PROTOTYPE:
       out = astro_constants(in)
    
     DESCRIPTION:
       Returns a constant corresponding to the input element.
    
       List of identifiers:
           Generic astronomical constants:
               1   Universal gravity constant (G) (from DITAN and Horizon) [km^3/(kg*s^2)]
               2   Astronomical Unit (AU) (from DE405) [km]
                   Note:  The value for 1 au is from the IAU 2012 Resolution B1.
           Sun related:
               3   Sun mean radius (from DITAN) [km]
               4   Sun planetary constant (mu = mass * G) (from DE405)
                   [km^3/s^2]
               31  Energy flux density of the Sun (from Wertz,SMAD)
                   [W/m2 at 1 AU]
           Other:
               5   Speed of light in the vacuum (definition in the SI and Horizon) [km/s]
               6   Standard free fall (the acceleration due to gravity on the
                   Earth's surface at sea level) (from Wertz,SMAD) [m/s^2]
               7   Mean distance Earth-Moon (from Wertz,SMAD) [km]
               8   Obliquity (angle) of the ecliptic at Epoch 2000 (from
                   Horizon) [rad]
               9   Gravitatonal field constant (J2) of the Earth (from Wertz,SMAD,
                   taken from JGM-2). This should be used in conjunction to
                   Earth radius = 6378.1363 km
               32  Days in a Julian year y = 365.25 d  (from Horizon)
           Planetary constants of the planets (mu = mass * G) [km^3/s^2]:
               11  Me      (from DE405)
               12  V       (from DE405)
               13  E       (from DE405)
               14  Ma      (from DE405)
               15  J       (from DE405)
               16  S       (from DE405)
               17  U       (from DE405)
               18  N       (from DE405)
               19  P       (from DE405)
               20  Moon    (from DE405)
           Mean radius of the planets [km]:
               21  Me      (from Horizon)
               22  V       (from Horizon)
               23  E       (from Horizon)
               24  Ma      (from Horizon)
               25  J       (from Horizon)
               26  S       (from Horizon)
               27  U       (from Horizon)
               28  N       (from Horizon)
               29  P       (from Horizon)
               30  Moon    (from Horizon)
    
       Notes for upgrading this function:
           It is possible to add new constants.
           - DO NOT change the structure of the function, as well as its
               prototype.
           - DO NOT change the identifiers of the constants that have already
               been defined in this function. If you want to add a new
               constant, use an unused identifier.
           - DO NOT add constants that can be easily computed starting form
               other ones (avoid redundancy).
    
     REFERENCES:
       - DITAN (Direct Interplanetary Trajectory Analysis), Massimiliano
           Vasile, 2006.
    	- Wertz J. R., Larson W. J., "Space Mission Analysis and Design", Third
           Edition, Space Technology Library 2003.
       [A]   DE405 - http://iau-comm4.jpl.nasa.gov/de405iom/de405iom.pdf
       [B]   Explanatory Supplement to the Astronomical Almanac. 1992. K. P.
             Seidelmann, Ed., p.706 (Table 15.8) and p.316 (Table 5.8.1),
             University Science Books, Mill Valley, California. 
       [C]   Tholen, D.J. and Buie, M.W. 1990. "Further Analysis of
             Pluto-Charon Mutual Event Observations" BAAS 22(3):1129.
       [D]   Seidelmann, P.K. et al. 2007. "Report of the IAU/IAG Working
             Group on cartographic coordinates and rotational elements: 2006"
             Celestial Mech. Dyn. Astr. 98:155-180. 
       [F]   Anderson, J.D., et al. 1987. "The mass, gravity field, and
             ephemeris of Mercury" Icarus 71:337-349.
       [G]   Konopliv, A.S., et al. 1999. "Venus gravity: 180th degree and
             order model" Icarus 139:3-18.
       [H]   Folkner, W.M. and Williams, J.G. 2008. "Mass parameters and
             uncertainties in planetary ephemeris DE421." Interoffice Memo.
             343R-08-004 (internal document), Jet Propulsion Laboratory,
             Pasadena, CA. 
       [I]   Jacobson, R.A. 2008. "Ephemerides of the Martian Satellites -
             MAR080" Interoffice Memo. 343R-08-006 (internal document),
             Jet Propulsion Laboratory, Pasadena, CA. 
       [J]   Jacobson, R.A. 2005. "Jovian Satellite ephemeris - JUP230"
             private communication. 
       [K]   Jacobson, R.A., et al. 2006. "The gravity field of the Saturnian
             system from satellite observations and spacecraft tracking data"
             AJ 132(6):2520-2526. 
       [L]   Jacobson, R.A. 2007. "The gravity field of the Uranian system and
             the orbits of the Uranian satellites and rings" BAAS 39(3):453. 
       [M]   Jacobson, R.A. 2008. "The orbits of the Neptunian satellites and
             the orientation of the pole of Neptune" BAAS 40(2):296. 
       [N]   Jacobson, R.A. 2007. "The orbits of the satellites of Pluto -
             Ephemeris PLU017" private communication.
       [W1]  http://ssd.jpl.nasa.gov/?planet_phys_par Last retrieved
             20/03/2013
       [W2]  http://ssd.jpl.nasa.gov/?sat_phys_par Last retrieved
             20/03/2013
       [W3]  http://ssd.jpl.nasa.gov/horizons.cgi Last retrieved
             20/03/2013
       [M1]  Bills, B.G. and Ferrari, A.J. 1977. ``A Harmonic Analysis of
             Lunar Topography'', Icarus 31, 244-259.
       [M2]  Standish, E. M. 1998. JPL Planetary and Lunar Ephemerides,
             DE405/LE405.
       [M3]  Lunar Constants and Models Document, Ralph B. Roncoli, 23 Sept 2005,
             JPL Technical Document D-32296 
    
    
     CALLED FUNCTIONS:
       (none)
    
     AUTHOR:
       Matteo Ceriotti, 2006, MATLAB, astroConstants.m
    
     PREVIOUS VERSIONS:
       Matteo Ceriotti, 2006, MATLAB, astro_constants.m, Ver. 1.2
           - Header and function name in accordance with guidlines.
       26/10/2006, Camilla Colombo: Updated.
       22/10/2007, Camilla Colombo: astroConstants(8) added (Obliquity (angle)
           of the ecliptic at Epoch 2000).
       02/10/2009, Camilla Colombo: Header and function name in accordance
           with guidlines.
       12/11/2010, Camilla Colombo: astroConstants(9) added (J2) Note: the
           present value of J2 is not consistent with the value of the Earth
           radius. This value of J2 should be used in conjunction to Earth
           radius = 6378.1363 km
       19/03/2013, Camilla Colombo: constants updated to NASA JPL website.
           References added.
       20/03/2013, REVISION, Francesca Letizia.
       22/03/2013, Francesca Letizia: all GM from DE405.

       CHANGELOG:
       26/05/2022, Christian Di Lazzaro: MATLAB function converted to Python function.
            It does not accept a list as input anymore: transformed into a single input-single
            output function.
    
     ------------------------------------------------------------------------

    Args:
        n (int): constant value identifying the astronomical constant to be returned.

    Raises:
        ValueError: risen when n does not match any gravitational constant.

    Returns:
        float: the gravitational constant corresponding to the input identifier.
    """

    if n == 1:
        out=6.67259e-20 # From DITAN and Horizon
    elif n == 2:
        out=149597870.691 # From DE405
    elif n == 3:
        # out=700000 # From DITAN
        out=6.955*10^5 # From Horizon [W3]
    elif n == 4:
        # out=0.19891000000000E+31*6.67259e-20 # From DITAN
        out=1.32712440017987E+11 # From DE405 [A]
    elif n == 5:
        out=299792.458 # Definition in the SI, Horizon, DE405
    elif n == 6:
        out=9.80665 # Definition in Wertz, SMAD
    elif n == 7:
        # out=384401 # Definition in Wertz, SMAD
        out=384400 # From Horizon [W3]
    elif n == 8:
        # out=23.43928111*pi/180 # Definition in Wertz, SMAD
        out=84381.412/3600*pi/180 # Definition in Horizon
        # obliquity of ecliptic (J2000)    epsilon = 84381.412 (± 0.005) arcsec 
    elif n == 9:
        out=0.1082626925638815e-2 # Definition in Wertz, SMAD
    elif n == 11:
        # out=0.33020000000000E+24*6.67259e-20 # From DITAN
        #out=0.330104E+24*6.67259e-20    # From Horizon [F]
        out=2.203208E+4    # From DE405
    elif n == 12:
        # out=0.48685000000000E+25*6.67259e-20 # From DITAN
        #out=4.86732E+24*6.67259e-20     # From Horizon [G]
        out=3.24858599E+5 # From DE405
    elif n == 13:
        # out=0.59736990612667E+25*6.67259e-20 # From DITAN
        # out=5.97219E+24*6.67259e-20     # From Horizon [H]
        out = 3.98600433e+5 # From DE405
    elif n == 14:
        # out=0.64184999247389E+24*6.67259e-20 # From DITAN
        #out=0.641693E+24*6.67259e-20 	# From Horizon [I]
        out = 4.2828314E+4 #Frome DE405
    elif n == 15:
        # out=0.18986000000000E+28*6.67259e-20 # From DITAN
        #out=1898.13E+24*6.67259e-20 	# From Horizon [J]
        out = 1.26712767863E+08 # From DE405
    elif n == 16:
        # out=0.56846000000000E+27*6.67259e-20 # From DITAN
        # out=568.319E+24*6.67259e-20     # From Horizon [k]
        out = 3.79406260630E+07 # From DE405
    elif n == 17:
        # out=0.86832000000000E+26*6.67259e-20 # From DITAN
        # out=86.8103E+24*6.67259e-20     # From Horizon [L]
        out= 5.79454900700E+06 # From DE405
    elif n == 18:
        # out=0.10243000000000E+27*6.67259e-20 # From DITAN
        # out=102.410E+24*6.67259e-20     # From Horizon [M]
        out = 6.83653406400E+06 # From DE405
    elif n == 19:
        # out=0.14120000000000E+23*6.67259e-20 # From DITAN
        #out=.01309E+24*6.67259e-20     # From Horizon [N]
        out = 9.81601000000E+02 #From DE405
    elif n == 20:
        # out=0.73476418263373E+23*6.67259e-20 # From DITAN
        out=4902.801                 # From Horizon  [M2]
        #out=4902.801076                # From Horizon  [M3]
    elif n == 21:
        # out=0.24400000000000E+04 # From DITAN
        out=2439.7 # From Horizon [D]
    elif n == 22:
        # out=0.60518000000000E+04 # From DITAN
        out=6051.8 # From Horizon [D]
    elif n == 23:
        # out=0.63781600000000E+04 # From DITAN
        # out=6371.00 # From Horizon [B]
        out=6371.01 # From Horizon [W3]
    elif n == 24:
        # out=0.33899200000000E+04 # From DITAN
        # out=3389.50 # From Horizon [D]
        out=3389.9 # From Horizon [W3]            
    elif n == 25:
        # out=0.69911000000000E+05 # From DITAN
        out=69911   # From Horizon [D]
    elif n == 26:
        # out=0.58232000000000E+05 # From DITAN
        out=58232   # From Horizon [D]
    elif n == 27:
        # out=0.25362000000000E+05 # From DITAN
        out=25362   # From Horizon [D]
    elif n == 28:
        # out=0.24624000000000E+05 # From DITAN
        # out=24622   # From Horizon [D]
        out= 24624 # From Horizon [W3]            
    elif n == 29:
        # out=0.11510000000000E+04 # From DITAN
        out=1151 	# From Horizon [C]
    elif n == 30:
        # out=0.17380000000000E+04 # From DITAN
        # out=1737.5  # From Horizon [M1]
        out=1738.0    # From Horizon  [M3]
    elif n == 31:
        out=1367 # From Wertz, SMAD
        # out=1367.6  # From Horizon  [W3]
    elif n == 32:
        out=365.25 # From Horizon
    # Add an identifier and constant here. Prototype:
    # elif n == $identifier$
    #     out=$constant_value$;
    else:
        raise ValueError(f'Constant identifier {n} is not defined!')
        out=0