#pragma once
#include "FixedCapBiMap.h"
class FixedCapBiMapIterator
{
	//DO NOT CHANGE THIS PART
	friend class FixedCapBiMap;
private:
	const FixedCapBiMap& map;
	int current; //pos of current element

	FixedCapBiMapIterator(const FixedCapBiMap& m);
public:
	void first();
	void next();
	TElem getCurrent();
	bool valid() const;
};


