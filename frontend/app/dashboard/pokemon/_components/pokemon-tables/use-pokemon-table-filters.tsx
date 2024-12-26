'use client';

import { searchParams } from '@/lib/searchparams';
import { useQueryState } from 'nuqs';
import { useCallback, useMemo } from 'react';

export function usePokemonTableFilters() {
  const [searchQuery, setSearchQuery] = useQueryState(
    'q',
    searchParams.q
      .withOptions({ shallow: false, throttleMs: 1000 })
      .withDefault('')
  );

  const [baseExperienceFilter, setBaseExperienceFilter] = useQueryState(
    'base_experience',
    searchParams.base_experience.withOptions({ shallow: false })
  );

  const [heightFilter, setHeightFilter] = useQueryState(
    'height',
    searchParams.height.withOptions({ shallow: false })
  );

  const [page, setPage] = useQueryState(
    'page',
    searchParams.page.withDefault(1)
  );

  const [sortOrder, setSortOrder] = useQueryState(
    'sort',
    searchParams.sort.withOptions({ shallow: false }).withDefault('asc')
  );

  const resetFilters = useCallback(() => {
    setSearchQuery(null);
    setBaseExperienceFilter(null);
    setHeightFilter(null);
    setSortOrder("asc");
    setPage(1);
  }, [setSearchQuery, setBaseExperienceFilter, setHeightFilter, setSortOrder, setPage]);

  const isAnyFilterActive = useMemo(() => {
    return !!searchQuery || !!baseExperienceFilter || !!heightFilter;
  }, [searchQuery, baseExperienceFilter, heightFilter]);

  return {
    searchQuery,
    setSearchQuery,
    baseExperienceFilter,
    setBaseExperienceFilter,
    heightFilter,
    setHeightFilter,
    page,
    setPage,
    resetFilters,
    isAnyFilterActive,
    sortOrder,
    setSortOrder,
  };
}
