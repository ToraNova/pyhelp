/*
 * Another library to show namespace doesn't collide
 * https://stackoverflow.com/questions/4396140/why-doesnt-ansi-c-have-namespaces
 */

#ifndef __OTHER_H__
#define __OTHER_H__

struct _other {
	const int tmp;
	void (*foo)(void);
	int (*bar)(int);
};

extern const struct _other another;

#endif
