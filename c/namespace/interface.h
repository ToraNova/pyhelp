/*
 * While c doesn't really support namespaces, I believe they are awesome and
 * am trying to see how to incorporate the style of namespaces into c projects
 * this is an example from
 * https://stackoverflow.com/questions/4396140/why-doesnt-ansi-c-have-namespaces
 */

#ifndef __INTERFACE_H__
#define __INTERFACE_H__

struct _library {
	const int tmp;
	void (*foo)(void);
	int (*bar)(int);
};

extern const struct _library library;

#endif
