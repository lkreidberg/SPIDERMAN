#include "ephemeris.h"
#include "math.h"
#include <stdlib.h>
#include <stdio.h>


double *separation_of_centers(double t, double tc, double per, double a, double inc, double ecc, double omega, double R_s, double Ratio){
	// based on equations in Winn 2010 (chapter of sara seager book same year)
	double r,f,M,n,tp,E,eps;
	double X,Y,Z;

	//have to scale a

	double solar_r = 6.957e8; // m
	double au = 1.4960e11; // m

	a = a*au;


	double stellar_r = solar_r*R_s;

	double image_scale = stellar_r/Ratio;

	n = 2.*M_PI/per;	// mean motion
	eps = 1.0e-7;

	inc = inc*M_PI/180.0; // translate inclination into radians

	f = M_PI/2. - omega;								//true anomaly corresponding to time of primary transit center
	E = 2.*atan(sqrt((1. - ecc)/(1. + ecc))*tan(f/2.));				//corresponding eccentric anomaly
	M = E - ecc*sin(E);						
	tp = tc - per*M/2./M_PI;							//time of periastron 

	if(ecc < 1.0e-5){
		f = ((t - tp)/per - (int)((t - tp)/per))*2.*M_PI;			//calculates f for a circular orbit
	}
	else{
		M = n*(t - tp);
		E = getE(M, ecc);
		f = 2.*atan(sqrt((1.+ecc)/(1.-ecc))*tan(E/2.));
	}


	r = a*(1-pow(ecc,2))/(1 + ecc*cos(f));

	X = -r*cos(omega + f);
	Y = -r*sin(omega + f)*cos(inc);
	Z = r*sin(omega + f)*sin(inc);

    double *coords = malloc(sizeof(double) *4); // dynamic `array (size 4) of pointers to int`

    coords[0] = X/image_scale;
    coords[1] = Y/image_scale;
    coords[2] = Z/image_scale;
    coords[3] = Z;

    return coords;
}

double getE(double M, double e)	//calculates the eccentric anomaly (see Seager Exoplanets book:  Murray & Correia eqn. 5 -- see section 3)
{
	double E = M, eps = 1.0e-7;

	while(fabs(E - e*sin(E) - M) > eps) E = E - (E - e*sin(E) - M)/(1.0 - e*cos(E));
	return E;
}