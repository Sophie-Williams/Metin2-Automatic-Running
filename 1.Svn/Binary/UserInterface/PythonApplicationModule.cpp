/// 1.) Find this:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

/// 2.) Add after this:
#if defined(ENABLE_AUTO_RUNING)
	PyModule_AddIntConstant(poModule, "ENABLE_AUTO_RUNING",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_AUTO_RUNING",	0);
#endif