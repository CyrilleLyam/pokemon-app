'use client';

import { DataTable } from '@/components/ui/table/data-table';
import { DataTableResetFilter } from '@/components/ui/table/data-table-reset-filter';
import { DataTableSearch } from '@/components/ui/table/data-table-search';
import { Pokemon } from '@/constants/data';
import { columns } from './columns';
import { usePokemonTableFilters } from './use-pokemon-table-filters';
import { Input } from '@/components/ui/input';
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from '@/components/ui/select'; // Assuming these components are from ShadCN
import { cn } from '@/lib/utils';

export default function PokemonTable({
  data,
  totalData,
}: {
  data: Pokemon[];
  totalData: number;
}) {
  const {
    searchQuery,
    setSearchQuery,
    baseExperienceFilter,
    setBaseExperienceFilter,
    heightFilter,
    setHeightFilter,
    resetFilters,
    isAnyFilterActive,
    setPage,
    sortOrder,
    setSortOrder,
  } = usePokemonTableFilters();

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-4">
        <DataTableSearch
          searchKey="name"
          searchQuery={searchQuery}
          setSearchQuery={setSearchQuery}
          setPage={setPage}
        />
        <Input
          id="base_experience"
          type="number"
          placeholder="Enter Base Experience"
          value={baseExperienceFilter || ''}
          onChange={(e: any) => setBaseExperienceFilter(e.target.value)}
          className={cn('w-full md:max-w-sm')}
        />
        <Input
          id="height"
          type="number"
          placeholder="Enter Height"
          value={heightFilter || ''}
          onChange={(e: any) => setHeightFilter(e.target.value)}
          className={cn('w-full md:max-w-sm')}
        />
        {/* ShadCN Select for Sort Order */}
        <Select value={sortOrder} onValueChange={setSortOrder}>
          <SelectTrigger className={cn('w-full md:max-w-sm')}>
            <SelectValue placeholder="Sort Order" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="asc">Ascending</SelectItem>
            <SelectItem value="desc">Descending</SelectItem>
          </SelectContent>
        </Select>
        <DataTableResetFilter
          isFilterActive={isAnyFilterActive}
          onReset={resetFilters}
        />
      </div>
      <DataTable columns={columns} data={data} totalItems={totalData} />
    </div>
  );
}
